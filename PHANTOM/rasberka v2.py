import sqlite3
import time
from datetime import datetime
import serial
import re
import pandas as pd  # NOWA BIBLIOTEKA DO EKSPORTU

# --- KONFIGURACJA POŁĄCZENIA I SPRZĘTU ---
SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 115200
DB_NAME = 'projekt_phantom_6g.db'
CSV_OUTPUT_FILE = 'pomiary_phantom_export.csv'  # PLIK WYJŚCIOWY DLA GENERATORA
EKSPORT_INTERVAL = 60  # Co ile sekund eksportować dane do CSV

CZĘSTOTLIWOŚĆ = 3.5
MOC = 10.0
NUMER_SONDY = 1
R_NOMINALNE = 10000.0
V_EX = 3.3
G_WZMACNIACZ = 100.0

# --- INICJALIZACJA PORTU SZEREGOWEGO (BEZ ZMIAN) ---
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
    print(f"✅ Pomyślnie połączono z ESP32 na porcie: {SERIAL_PORT}")
except serial.SerialException as e:
    print(f"❌ Błąd: Nie można połączyć z ESP32. Błąd: {e}")
    exit()


# --- FUNKCJE BAZY DANYCH I KONWERSJI (BEZ ZMIAN) ---
def inicjalizuj_db(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pomiary_phantom (
            timestamp DATETIME NOT NULL,
            sonda INTEGER NOT NULL,
            volt REAL NOT NULL,        
            freq REAL NOT NULL,       
            moc REAL NOT NULL
        )
    """)
    conn.commit()
    return conn


def mv_na_impedancje(mv_value):
    V_wy_wzmocnione = mv_value / 1000.0
    R_delta = V_wy_wzmocnione * (4.0 * R_NOMINALNE) / (V_EX * G_WZMACNIACZ)
    return R_delta


def zaloguj_dane(conn, sonda_nr, mv, freq, moc):
    volt_value = mv / 1000.0
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO pomiary_phantom (timestamp, sonda, volt, freq, moc)
            VALUES (?, ?, ?, ?, ?)
        """, (timestamp, sonda_nr, volt_value, freq, moc))
        conn.commit()
        impedancja_test = mv_na_impedancje(mv)
        print(
            f"💾 Zapisano: {timestamp} | {volt_value:.6f} V | Freq: {freq} GHz | Impedancja: {impedancja_test:.4f} Ohm")
    except Exception as e:
        print(f"❌ Błąd zapisu do bazy danych: {e}")


# --- NOWA FUNKCJA EKSPORTU DO GENERATORA ---
def eksportuj_do_csv(db_conn, output_file):
    """Odczytuje wszystkie dane z bazy SQL i zapisuje je do pliku CSV."""
    try:
        # Wczytanie całej tabeli do obiektu Pandas DataFrame
        df = pd.read_sql_query("SELECT * FROM pomiary_phantom", db_conn)

        # Zapis do pliku CSV
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"\n📢 Eksport danych do CSV zakończony! Plik: {output_file}")
    except Exception as e:
        print(f"❌ Błąd eksportu: {e}")


# --- GŁÓWNA PĘTLA PROGRAMU Z EKSPORTEM ---
if __name__ == "__main__":

    conn = inicjalizuj_db(DB_NAME)
    print("\n--- Rozpoczynanie logowania danych z ESP32 ---")

    ostatni_eksport = time.time()  # Inicjalizacja licznika czasu

    try:
        while True:
            # BLOKUJĄCY ODCZYT: Odbiór danych z ESP32
            line = ser.readline().decode('utf-8').strip()

            if line:
                try:
                    if ',' not in line and re.match(r"^-?\d+(\.\d+)?$", line):
                        mv_value = float(line)
                    elif ',' in line:
                        parts = line.split(',')
                        if len(parts) == 2 and parts[0].startswith('Sonda'):
                            mv_value = float(parts[1])
                        else:
                            print(f"⚠️ Nieznany format danych: {line}")
                            continue
                    else:
                        print(f"⚠️ Odrzucono nieznany format danych: {line}")
                        continue

                    # 1. Zapis do SQL (główna operacja)
                    zaloguj_dane(conn, NUMER_SONDY, mv_value, CZĘSTOTLIWOŚĆ, MOC)

                    # 2. Sprawdzenie, czy minął czas na eksport
                    if time.time() - ostatni_eksport >= EKSPORT_INTERVAL:
                        eksportuj_do_csv(conn, CSV_OUTPUT_FILE)
                        ostatni_eksport = time.time()  # Reset licznika

                except ValueError:
                    print(f"❌ Błąd konwersji liczby (sprawdź format danych z ESP32): {line}")
                except Exception as e:
                    print(f"❌ Nieoczekiwany błąd przetwarzania: {e}")

    except KeyboardInterrupt:
        print("\n\n🛑 Przerwanie przez użytkownika. Wykonywanie końcowego eksportu...")
        # WYKONANIE KOŃCOWEGO EKSPORTU PRZED ZAMKNIĘCIEM
        eksportuj_do_csv(conn, CSV_OUTPUT_FILE)

    finally:
        ser.close()
        conn.close()
        print("✅ Połączenia zamknięte. Koniec programu.")