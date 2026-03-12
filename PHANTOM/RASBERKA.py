import sqlite3
import time
from datetime import datetime
import serial
import re

SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 115200
DB_NAME = 'projekt_phantom_6g.db'

CZĘSTOTLIWOŚĆ = 3.5
MOC = 10.0
NUMER_SONDY = 1

R_NOMINALNE = 10000.0
V_EX = 3.3
G_WZMACNIACZ = 100.0

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
    print(f"✅ Pomyślnie połączono z ESP32 na porcie: {SERIAL_PORT} (Prędkość: {BAUD_RATE})")
except serial.SerialException as e:
    print(f"❌ Błąd: Nie można połączyć z ESP32 na {SERIAL_PORT}. Sprawdź kabel i port. Błąd: {e}")
    exit()

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

if __name__ == "__main__":

    conn = inicjalizuj_db(DB_NAME)
    print("\n--- Rozpoczynanie logowania danych z ESP32 ---")

    try:
        while True:
            if ser.in_waiting > 0:
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

                        zaloguj_dane(conn, NUMER_SONDY, mv_value, CZĘSTOTLIWOŚĆ, MOC)

                    except ValueError:
                        print(f"❌ Błąd konwersji liczby (sprawdź format danych z ESP32): {line}")
                    except Exception as e:
                        print(f"❌ Nieoczekiwany błąd przetwarzania: {e}")

            time.sleep(0.01)

    except KeyboardInterrupt:
        print("\n\n🛑 Przerwanie przez użytkownika. Zamykanie połączeń.")
    finally:
        ser.close()
        conn.close()
        print("✅ Połączenia zamknięte. Koniec programu.")