plik = open("test.txt","a")
if plik.writable():
    plik.write(input("Wprowadź tekst: "))
    print("\n")
plik.close()

plik = open("test.txt","r")

if plik.readable():
    print(plik.read())
    tekst = plik.readlines()
    print(tekst)
    for x in tekst:
        print(x)
