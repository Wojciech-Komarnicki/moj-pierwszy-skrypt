import os

def wyczysc_konsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def dodawanie(ilość_punktów_gracza):
    if True:
        ilość_punktów_gracza+=1
    return ilość_punktów_gracza

try:
    ilość_punktów_gracza =0
    ilość_maksymalnych_punktów = 3
    list = []
    a = input("Ile planet jest w układzie słoneczym?: ")
    wyczysc_konsole()
    b = input("Ile gwiazd jest w układzie słonecznym?: ")
    wyczysc_konsole()
    c = input("Którą licząc od słońca planetą jest ziemia?: ")
    wyczysc_konsole()

    if a == "8":
        ilość_punktów_gracza=dodawanie(ilość_punktów_gracza)
        a=a+" dobra odpowiedź"
    else:
        a=a+" zła odpowiedź"
    if b=="1":
        ilość_punktów_gracza=dodawanie(ilość_punktów_gracza)
        b=b+" dobra odpowiedź"
    else:
        b=b+" zła odpowiedź"
    if c=="3":
        ilość_punktów_gracza=dodawanie(ilość_punktów_gracza)
        c=c+" dobra odpowiedź"
    else:
        c=c+" zła odpowiedź"


    list.extend([a,b,c])
    print(f"Twój wynik to: {ilość_punktów_gracza} na {ilość_maksymalnych_punktów}")
    print("-------------------------------------------")
    for numer, odpowiedz in enumerate(list, 1):
        print("Pytanie nr {}. Twoja odpowiedz: {}".format(numer, odpowiedz))
except ValueError as e:
    print(e)
except Exception as e:
    print(e)