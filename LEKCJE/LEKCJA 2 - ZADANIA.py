a = float(input("Podaj cene produktu: "))
b = int(input("Podaj ilość sztuk: "))
c = int(input("Podaj ile zapłacisz w banknocie (nie licząc reszty): "))
print(f"Całkowity koszt zakupu to: {a*b}")
print(f"Reszta: {c-a*b} ")

