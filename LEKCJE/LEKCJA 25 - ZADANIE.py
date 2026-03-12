# from operator import truediv
#
# #zad 1
# class KontoBankowe:
#     liczba_kont=0
#     def __init__(self, wlasciciel: str, saldo: float = 0.0):
#         self.wlasciciel = wlasciciel
#         self.saldo = saldo
#         KontoBankowe.liczba_kont += 1
#
#     def wplata(self,kwota: float):
#         if kwota<=0:
#             return "Wpłacona kwota musi być większa od 0"
#
#         self.saldo += kwota
#         return f"Wpłacono {kwota:.2f} zł. Nowe saldo: {self.saldo:.2f}"
#
#     def wyplata(self,kwota: float):
#         if kwota<=0:
#             return "Wypłacona kwota musi być większa od 0"
#         if self.saldo >= 0:
#             self.saldo -= kwota
#             return f"Została wypłacona kwota: {kwota:.2f} zł. Nowe saldo: {self.saldo:.2f} zł"
#         else:
#             return f"Niewystarczająco dużo środków na koncie. Dostępna saldo: {self.saldo:.2f} zł "
#
# while True:
#     print("1. Dodaj konto")
#     print("2. Wplata na konto")
#     print("3. Wyplata z konta")
#     wybor = input("Wybor: ")
#
# #zad 2

class Samochod:
    def __init__(self, marka: str, model: str, rok_produkcji: int):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
    def wyswietl_info(self):
        return f"Marka: {self.marka}\nModel: {self.model}\nRok produkcji: {self.rok_produkcji}"



#zad 3

class LuksusowySamochod(Samochod):
    def __init__(self, marka: str, model: str, rok_produkcji: int, cena_wyjsciowa: float):
        super().__init__(marka, model, rok_produkcji)
        self.cena_wyjsciowa = cena_wyjsciowa

    def wyswietl_info(self):
        podstawowe_info = super().wyswietl_info()
        pelne_info = podstawowe_info + f"\nCena wyjsciowa: {self.cena_wyjsciowa}"
        return pelne_info


moj_samochod = Samochod("Fiat", "Punciak", 1995)
print(moj_samochod.wyswietl_info())
print('')

moj_luksusowy_samochod = LuksusowySamochod("Fiat", "Punciak", 1995, 2345)
print(moj_luksusowy_samochod.wyswietl_info())