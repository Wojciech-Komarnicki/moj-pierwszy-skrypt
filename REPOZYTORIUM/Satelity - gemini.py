import os
import sys
import glob


def pobierz_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except Exception as e:
            print("Błędne dane! Podaj poprawną liczbę.")


class Satelita:
    def __init__(self, nazwa: str, wysokosc_orbity: float, predkosc: float, czas_zycia: float):
        self.nazwa = nazwa
        self.wysokosc_orbity = wysokosc_orbity
        self.predkosc = predkosc
        self.czas_zycia = czas_zycia

    def __str__(self) -> str:
        return (
            f"Nazwa: {self.nazwa}\n"
            f"Wysokosc orbity: {self.wysokosc_orbity} km\n"
            f"Predkosc: {self.predkosc} km/s\n"
            f"Czas zycia orbity: {self.czas_zycia} lat\n"
            "------------------------"
        )

    def wyswietl_info(self):
        print(self)

    def pobierz_nazwe(self) -> str:
        return self.nazwa

    def pobierz_wysokosc_orbity(self) -> float:
        return self.wysokosc_orbity

    def pobierz_predkosc(self) -> float:
        return self.predkosc

    def edytuj_info(self):
        print(f"Edycja informacji dla satelity: {self.nazwa}")
        self.wysokosc_orbity = pobierz_float("Nowa wysokosc orbity (w kilometrach): ")
        self.predkosc = pobierz_float("Nowa predkosc satelity (w km/s): ")
        self.czas_zycia = pobierz_float("Nowy czas zycia orbity (w latach): ")

    def do_zapisu(self) -> str:
        return f"Satelita {self.nazwa} {self.wysokosc_orbity} {self.predkosc} {self.czas_zycia}"


class SatelitaKomunikacyjny(Satelita):
    def __init__(self, nazwa: str, wysokosc_orbity: float, predkosc: float, czas_zycia: float, czestotliwosc: str):
        super().__init__(nazwa, wysokosc_orbity, predkosc, czas_zycia)
        self.czestotliwosc = czestotliwosc

    def __str__(self) -> str:
        base_info = super().__str__()
        base_lines = base_info.split('\n')[:-1]
        base_lines.append(f"Czestotliwosc: {self.czestotliwosc}")
        base_lines.append("------------------------")
        return "\n".join(base_lines)

    def edytuj_info(self):
        super().edytuj_info()
        self.czestotliwosc = input("Nowa czestotliwosc komunikacji (bez spacji): ")

    def do_zapisu(self) -> str:
        return f"SatelitaKom {self.nazwa} {self.wysokosc_orbity} {self.predkosc} {self.czas_zycia} {self.czestotliwosc}"


def zapisz_do_pliku(katalog: list, nazwa_pliku: str):
    nazwa_pliku_z_txt = nazwa_pliku + ".txt"
    try:
        with open(nazwa_pliku_z_txt, 'w', encoding='utf-8') as plik:
            for satelita in katalog:
                plik.write(satelita.do_zapisu() + "\n")
        print(f"Katalog został zapisany do pliku: {nazwa_pliku_z_txt}")
    except IOError as e:
        print(f"Błąd przy próbie zapisu do pliku: {e}")


def pobierz_dostepne_pliki() -> list:
    print("Dostępne pliki .txt:")
    dostepne_pliki = glob.glob("*.txt")
    if not dostepne_pliki:
        print("Brak plików .txt w katalogu.")
    else:
        for plik in dostepne_pliki:
            print(f"- {plik}")
    return dostepne_pliki


def wczytaj_z_pliku(katalog: list, nazwa_pliku: str):
    katalog.clear()
    nazwa_pliku_z_txt = nazwa_pliku + ".txt"
    try:
        with open(nazwa_pliku_z_txt, 'r', encoding='utf-8') as plik:
            for linia in plik:
                czesci = linia.strip().split()
                if not czesci:
                    continue

                typ_satelity = czesci[0]
                dane = czesci[1:]

                try:
                    if typ_satelity == "Satelita" and len(dane) == 4:
                        nazwa, wys, pred, czas = dane
                        katalog.append(Satelita(nazwa, float(wys), float(pred), float(czas)))
                    elif typ_satelity == "SatelitaKom" and len(dane) == 5:
                        nazwa, wys, pred, czas, czest = dane
                        katalog.append(SatelitaKomunikacyjny(nazwa, float(wys), float(pred), float(czas), czest))
                    else:
                        print(f"Ostrzeżenie: Nieprawidłowy format linii w pliku: {linia.strip()}")
                except Exception as e:
                    print(f"Błąd przetwarzania linii: {linia.strip()} -> {e}")
            print(f"Katalog został wczytany z pliku: {nazwa_pliku_z_txt}")
    except FileNotFoundError:
        print(f"Błąd: Plik '{nazwa_pliku_z_txt}' nie istnieje.")
    except IOError as e:
        print(f"Błąd przy próbie odczytu pliku: {e}")


def usun_satelite(katalog: list, nazwa: str):
    znaleziono = False
    i = 0
    while i < len(katalog):
        if katalog[i].pobierz_nazwe() == nazwa:
            katalog.pop(i)
            znaleziono = True
            print(f"Satelita {nazwa} został usunięty.")
            break
        else:
            i += 1

    if not znaleziono:
        print(f"Satelita o nazwie {nazwa} nie istnieje w katalogu.")


def wyswietl_statystyki(katalog: list):
    if not katalog:
        print("Katalog jest pusty. Brak statystyk.")
        return

    suma_wysokosci_orbity = sum(s.pobierz_wysokosc_orbity() for s in katalog)
    max_predkosc = max(s.pobierz_predkosc() for s in katalog)
    liczba_satelitow = len(katalog)
    srednia_wysokosc_orbity = suma_wysokosci_orbity / liczba_satelitow

    print("Statystyki Katalogu:")
    print(f"Srednia wysokosc orbity: {srednia_wysokosc_orbity:.2f} km")
    print(f"Maksymalna predkosc: {max_predkosc} km/s")
    print(f"Liczba satelitow: {liczba_satelitow}")


def main():
    katalog_satelitow = [
        Satelita("ISS", 420, 7.66, 34),
        Satelita("Teleskop_Hubble'a", 547, 7.66, 35),
        Satelita("Satelity_GPS", 20200, 3.89, 10),
        SatelitaKomunikacyjny("Astra_1KR", 20200, 2.5, 10, "1.023_MHz"),
        Satelita("Landsat_8", 705, 7.61, 20),
        Satelita("GOES-16", 35786, 3.07, 15),
        Satelita("Satelity_Starlink", 550, 2.52, 20),
        Satelita("Landsat_10", 834, 7.66, 15)
    ]

    while True:
        print("\nMenu:")
        print("1. Dodaj satelite")
        print("2. Wyswietl katalog")
        print("3. Zapisz do pliku")
        print("4. Edytuj satelite")
        print("5. Statystyki katalogu")
        print("6. Usun satelite")
        print("8. Wczytaj z pliku")
        print("7. Wyjscie")

        wybor = input("Wybierz opcje: ")

        if wybor == '1':
            typ_satelity = ""
            while typ_satelity not in ("1", "2"):
                typ_satelity = input("Podaj typ satelity (1.Podstawowy / 2.Komunikacyjny). Wpisz 1 lub 2: ")
                if typ_satelity not in ("1", "2"):
                    print("Nieprawidłowy typ satelity.")

            print("UWAGA: Nazwy i częstotliwości nie mogą zawierać spacji.")
            nazwa = input("Podaj nazwe satelity (bez spacji): ")
            wysokosc_orbity = pobierz_float("Podaj wysokosc orbity (w kilometrach): ")
            predkosc = pobierz_float("Podaj predkosc satelity (w km/s): ")
            czas_zycia = pobierz_float("Podaj czas zycia orbity (w latach): ")

            if typ_satelity == "1":
                katalog_satelitow.append(Satelita(nazwa, wysokosc_orbity, predkosc, czas_zycia))
            elif typ_satelity == "2":
                czestotliwosc = input("Podaj czestotliwosc komunikacji (bez spacji): ")
                katalog_satelitow.append(
                    SatelitaKomunikacyjny(nazwa, wysokosc_orbity, predkosc, czas_zycia, czestotliwosc))
            print(f"Satelita '{nazwa}' został dodany.")

        elif wybor == '2':
            if not katalog_satelitow:
                print("Katalog jest pusty.")
            else:
                for satelita in katalog_satelitow:
                    satelita.wyswietl_info()

        elif wybor == '3':
            nazwa_pliku = input("Podaj nazwe pliku do zapisu (bez .txt): ")
            zapisz_do_pliku(katalog_satelitow, nazwa_pliku)

        elif wybor == '4':
            if not katalog_satelitow:
                print("Katalog jest pusty. Nie ma satelitów do edycji.")
            else:
                print("Dostepne satelity do edycji:")
                for satelita in katalog_satelitow:
                    print(f"- {satelita.pobierz_nazwe()}")

                nazwa_do_edycji = input("Podaj nazwe satelity do edycji: ")

                znaleziono = None
                for satelita in katalog_satelitow:
                    if satelita.pobierz_nazwe() == nazwa_do_edycji:
                        znaleziono = satelita
                        break

                if znaleziono:
                    znaleziono.edytuj_info()
                    print("Satelita został edytowany.")
                else:
                    print(f"Satelita o nazwie {nazwa_do_edycji} nie istnieje w katalogu.")

        elif wybor == '5':
            wyswietl_statystyki(katalog_satelitow)

        elif wybor == '6':
            if not katalog_satelitow:
                print("Katalog jest pusty. Nie ma satelitów do usuniecia.")
            else:
                print("Dostepne satelity do usuniecia:")
                for satelita in katalog_satelitow:
                    print(f"- {satelita.pobierz_nazwe()}")

                nazwa_do_usuniecia = input("Podaj nazwe satelity do usuniecia: ")
                usun_satelite(katalog_satelitow, nazwa_do_usuniecia)

        elif wybor == '8':
            pobierz_dostepne_pliki()
            nazwa_pliku = input("Podaj nazwe pliku do wczytania (bez .txt): ")
            wczytaj_z_pliku(katalog_satelitow, nazwa_pliku)

        elif wybor == '7':
            print("Do widzenia!")
            break

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

        input("\nNaciśnij Enter, aby kontynuować...")
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()