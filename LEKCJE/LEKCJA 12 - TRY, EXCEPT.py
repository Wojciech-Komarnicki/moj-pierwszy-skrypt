x = 12
y = 0
lista =[]
try:
    print(lista[2])
    print(x/y)
    print(x + "!")
except Exception as blad:
    print("Wystąpił błąd: ", blad)
    print("Typ błędu to:", type(blad).__name__)
finally:
    print("Instrukcja po")
