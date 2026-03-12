from random import randint

los = randint(1,5)

odp=0
liczenie_prob = 0
print("Zgadnij liczbe od 1 do 5")

while odp != los:
    liczenie_prob+=1
    odp=int(input("Podaj liczbe: "))
    if odp == los:
        break

print(f"Udało się! Zgadłeś!! Wylosowaną liczbą było: {los}")
print(f"Ilość twoich prób to {liczenie_prob}")