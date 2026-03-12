#Zad 1. ODliczenia od 1 do 15

# i = 0
# while i < 15:
#     i = i + 1
#     print(i)
#     if i>=15:
#         break
# print("KONIEC")

#Zad 2. Wyswietlanie liczb niepatrzysch od 1 do 20

# i = 0
# while i < 20:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)
# print("KONIEC")

#zad 3 Podanie liczb i ich ssumowanie

i=0
suma=0
while True:
    a = int(input("Napisz liczbe całkowitą: "))
    if 100>=a>=0:
        suma=suma+a
    elif a>100:
        continue
    else:
        break
print(suma)