slownik = {1: "Poniedzialek", 2: "Wtorek", 7: "Niedziela"}
print(slownik[1])
print(slownik[2])
print(slownik)
slownik[3] = "Sroda"
print(slownik[3])
slownik[4] = False
slownik["a"]=1
print(slownik)
slownik[8] = "twoja stara"

print(slownik.get(8, "Inny dzien"))

print("\nPętla: ")
for l in slownik.values():
    print(l)

print("\n--------------")
print(slownik.pop(8))
print(slownik)
#for klucz in sorted(slownik):
#   print(f"{klucz}: {slownik[klucz]}")

