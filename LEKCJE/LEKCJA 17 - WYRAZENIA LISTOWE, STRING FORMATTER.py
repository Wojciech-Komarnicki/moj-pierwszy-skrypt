lista = list(range(0,9))
print(lista)

nowa = [i*2 for i in lista]
nowa2 = [i for i in lista if i % 2 == 0]

print(nowa)
print(nowa2)

#formatowanie ciągów string

argumenty= ["Wojtek", 24]
tekst = "Czesc mam na imie {0} i mam {1} lat.".format(argumenty[0], argumenty[1])
tekst2 = "Czesc mam na imie {imie} i mam {wiek} lat.".format(imie = argumenty[0], wiek = argumenty[1])

print(tekst)
print(tekst2)