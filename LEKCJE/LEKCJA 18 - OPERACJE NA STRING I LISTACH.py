a=1
lista = [a,2,3,4]
print(lista)

print(", ".join(["a","b","c","d","e","f"]))
print("Witaj Witaj Świecie hejo".replace("Witaj","cześć"))

print("To jest zdanie".startswith("To")) #True
print("To jest zdanie".startswith("To lala")) #False

print("To jest zdanie".endswith("zdanie")) #True
print("To jest zdanie".endswith("To")) #False

print("jest" in "To jest zdanie") #True
print("ó" in "To jest zdanie") #False

print("To jest zdanie.".upper())
print("To jest zdanie.".lower())

print("----------------")
lista2 = [10, 20, 25, 35, 40]
if all([i % 2 == 0 for i in lista2]):
    print("Wszystkie są parzyste")
else:
    print("Nie wszystkie liczby są parzyste")

if any([i % 2 == 0 for i in lista2]):
    print("Conajmniej jedna z liczb jest parzysta")
else:
    print("Żadna z liczb nie jest parzysta")

for i in enumerate(lista2,1):
    print(i)

# for i in enumerate(lista2):
#     print(i[0]+1,"-", i[1])