from random import randint

liczba_losow=0
los = randint(1,10)
odp = 0
while True:
    odp=int(input("\nPodaj liczbę: "))
    liczba_losow += 1
    if liczba_losow >= 5:
        print("Wykorzystałeś wszystkie 5 losów! KONIEC")
        break
    if odp == los:
        print(f"WYGRAŁEŚ! Poprawną cyfrą była {los}. Liczba prób wyniosła: {liczba_losow}")
        break
    if odp!=los:
        print("Błąd!")
    if odp > los:
        print("Twoja odpowiedź jest większa od wylosowanej liczby")
    if odp < los:
        print("Twoja odpowiedź jest mniejsza od wylosowanej liczby")


