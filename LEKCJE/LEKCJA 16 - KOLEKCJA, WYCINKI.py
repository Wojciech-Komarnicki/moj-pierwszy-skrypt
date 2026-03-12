krotka = (2, 4, 8, 16, 32, 64, 128)
print(krotka)
print(krotka[6])

try:
    print("Elementów: ", krotka.count(8))
    print('Index: ', krotka.index(643))
except Exception as e:
    print(f"Wystąpił błąd {e}")

print("\nWycinki: ")
print(krotka[1:3])
print(krotka[-4:-2])
print(len(krotka))
print(krotka[0: 7:2])