import time
import os


def wyczysc_konsole():
    os.system('cls' if os.name == 'nt' else 'clear')

numery_mieszkan = [1,2,3,4]
poprawne_kody=[1234, 4567, 2137,9436]
while True:
    try:

        a = int(input("Numer mieszkania: "))
        wyczysc_konsole()
        if a in numery_mieszkan:
            wpisz_kod = int(input("Wpisz kod: "))
            wyczysc_konsole()
            if wpisz_kod == poprawne_kody[a-1]:
                print("Otwarte. Proszę wejść")
                for i in range(5, 0, -1):
                    wynik = f"Otwarte przez: {i}"
                    print('\r' + wynik, end="")
                    time.sleep(1)
                wyczysc_konsole()
            else:
                print("Niepoprawny kod")
                time.sleep(1)
                wyczysc_konsole()
        else:
            print("Mieszkanie nie istnieje")
            time.sleep(1)
            wyczysc_konsole()
    except Exception as e:
        print(e)
        time.sleep(0.5)
        wyczysc_konsole()