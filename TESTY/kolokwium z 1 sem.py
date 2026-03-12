import numpy as np
class Worek:
    def __init__(self, nazwa = "brak", kolor = "brak", zawartosc = None, masa = 0):
        self.nazwa = nazwa
        self.kolor = kolor
        if zawartosc is None:
            self.zawartosc = []
        else:
            self.zawartosc = zawartosc
        self.masa = masa
    def dodaj_przedmiot(self, nazwa_przedmiotu, masa_przedmiotu):
        przedmiot = (nazwa_przedmiotu, masa_przedmiotu)
        self.zawartosc.append(przedmiot)
        self.masa += masa_przedmiotu

    def postaw_na_wadze(self):
        aktualna_waga = self.masa
        print(f"Aktualna waga worka wynosi: {aktualna_waga} kg")
    def info(self):
        print(f"W worku: {self.nazwa}, znajdują się następujące przedmioty:")
        if self.zawartosc:
            for nazwa, masa in self.zawartosc:
                print(f"  - {nazwa}: {masa} kg")
            print(f"Łączna masa worka: {self.masa} kg\n")
        else:
            print("  - Worek jest pusty.")

worek_swietego_mikolaja = Worek(nazwa = "Prezenty", kolor = "czerwony")
worek_z_koksem = Worek(nazwa = "Koks", kolor = "biały")

worek_swietego_mikolaja.dodaj_przedmiot("lalka", 1)
worek_swietego_mikolaja.dodaj_przedmiot("samochod", 2)
worek_z_koksem.dodaj_przedmiot("marysia", 3)

worek_swietego_mikolaja.info()
worek_z_koksem.info()