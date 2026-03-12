import sqlite3
import time
from datetime import datetime
import random

# --- KONFIGURACJA PROJEKTU I SPRZĘTU (NOWE ZMIENNE) ---
DB_NAME = 'projekt_phantom_6g.db'
NUMER_SESJI = 1

# NOWE: Częstotliwość i Moc są teraz PRAWIDŁOWYMI typami float
CZĘSTOTLIWOŚĆ = 3.5  # GHz (float)
MOC = 10.0  # dBm (float)

# STAŁE FIZYCZNE MOSTKA WHEATSTONE'A
R_NOMINALNE = 10000.0
V_EX = 3.3
G_WZMACNIACZ = 100.0


# --- FUNKCJA SYMULUJĄCA ODCZYT Z ESP32 (BEZ ZMIAN) ---
def symuluj_odczyt_esp():
    """Zwraca losową linię danych w formacie "SondaX,mV_value"."""
    mv_value = round(random.uniform(10.00, 25.00), 4)
    sonda_nr = 1
    return f"Sonda{sonda_nr},{mv_value}"


# --- FUNKCJA KONWERSJI mV NA IMPEDANCJĘ/REZYSTANCJĘ (BEZ ZMIAN) ---
def mv_na_impedancje(mv_value):
    V_wy_wzmocnione = mv_value / 1000.0
    R_delta = V_wy_wzmocnione * (4.0 * R_NOMINALNE) / (V_EX * G_WZMACNIACZ)
    return R_delta


# --- DEFINICJA BAZY DANYCH (NOWA STRUKTURA) ---
def inicjalizuj_db(db_name):
    """Łączy się z bazą danych i tworzy tabelę o strukturze: (time, sonda, volt, freq, moc)"""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Utworzenie tabeli z DOKŁADNIE wymaganymi kolumnami
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


# --- FUNKCJA ZAPISU DO BAZY DANYCH (NOWE LOGOWANIE) ---
def zaloguj_dane(conn, sonda_nr, mv, freq, moc):
    """Przetwarza mV na V i zapisuje kompletny wiersz do bazy SQLite."""

    # 1. Przetwarzanie mV na V
    volt_value = mv / 1000.0

    # 2. Formatowanie znacznika czasu
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    cursor = conn.cursor()
    try:
        # Krok SQL: Wstawienie danych do kolumn: (time, sonda, volt, freq, moc)
        cursor.execute("""
            INSERT INTO pomiary_phantom (timestamp, sonda, volt, freq, moc)
            VALUES (?, ?, ?, ?, ?)
        """, (timestamp, sonda_nr, volt_value, freq, moc))

        conn.commit()

        print(f"💾 Zapisano: {timestamp} | Sonda {sonda_nr} | {volt_value:.6f} V | Freq: {freq} GHz | Moc: {moc} dBm")

    except Exception as e:
        print(f"❌ Błąd zapisu do bazy danych: {e}")


# --- GŁÓWNA PĘTLA PROGRAMU ---
if __name__ == "__main__":

    conn = inicjalizuj_db(DB_NAME)
    print("--- Rozpoczynanie logowania danych z SYMULACJI ESP32 ---")

    try:
        while True:
            # 1. POBIERANIE SYMULOWANEJ LINII
            line = symuluj_odczyt_esp()

            if line:
                try:
                    # Parsowanie danych wejściowych
                    parts = line.split(',')
                    if len(parts) == 2 and parts[0].startswith('Sonda'):
                        sonda_nr = int(parts[0].replace('Sonda', ''))
                        mv_value = float(parts[1])

                        # 2. Wywołanie funkcji zapisującej z parametrami FREQ i MOC
                        zaloguj_dane(conn, sonda_nr, mv_value, CZĘSTOTLIWOŚĆ, MOC)

                except Exception as e:
                    print(f"❌ Błąd przetwarzania: {e}")

            time.sleep(1)  # Zapisujemy jeden pomiar co sekundę

    except KeyboardInterrupt:
        print("\n\n🛑 Przerwanie przez użytkownika. Zamykanie połączeń.")
    finally:
        conn.close()
        print("✅ Połączenie z bazą danych zamknięte. Koniec programu.")