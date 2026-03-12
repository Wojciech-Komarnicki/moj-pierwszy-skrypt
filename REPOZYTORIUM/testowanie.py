import os
import time

def wyczyść_ekran():
    """Czyści ekran konsoli (kompatybilne z Windows, Linux, macOS)."""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/macOS
        os.system('clear')

# --- Start programu ---

# 1. Poproś o pierwszą daną
imię = input("Podaj swoje imię: ")

# Dodaj krótką przerwę, żeby użytkownik zobaczył, co się dzieje
time.sleep(1)

# 2. Wyczyść cały ekran (poprzedni komunikat i wprowadzone imię znikają)
wyczyść_ekran()

# 3. Poproś o kolejną daną (pojawi się na czystym ekranie)
nazwisko = input("Podaj swoje nazwisko: ")

# --- Koniec programu ---

print(f"\nDane zapisane:\nImię: {imię}\nNazwisko: {nazwisko}")