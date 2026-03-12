def transakcja(cena_za_przedmiot,poziom_inteligencji):
    if cena_za_przedmiot <= poziom_inteligencji:
        print("Scraftowano")
    elif cena_za_przedmiot > poziom_inteligencji:
        print(f"Wymaga {o_ile_wiecej} punktów inteligencji więcej")
    else:
        print("Błąd")


try:
    co_chce_zrobic=float(input("Co chcesz zrobić?\n1.Młotek\n2.Sikierę\n3.Łopatę\nWybierz: "))

    poziom_inteligencji = float(input("Ilość twoich punktów inteligencji: "))
    wymagany_poziom = 25
    młotek = 40
    siekiera=30
    łopata=20

    cena_za_przedmiot = 0

    if co_chce_zrobic == 1:
        cena_za_przedmiot = młotek
    elif co_chce_zrobic == 2:
        cena_za_przedmiot = siekiera
    elif co_chce_zrobic == 3:
        cena_za_przedmiot=łopata
    else:
        print("Poprawna opcja to: 1 lub 2 lub 3")
    o_ile_wiecej= cena_za_przedmiot - poziom_inteligencji
    transakcja(cena_za_przedmiot, poziom_inteligencji)



except ValueError:
    print("To musi być liczba")

except Exception as ex:
    print(ex)



