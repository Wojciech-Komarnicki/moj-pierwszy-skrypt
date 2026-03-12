lista = [1,2,4,2 ]
print(lista)
print(lista[1])
lista[2] = 3
print(lista)
tekst = "twoja stara"
print(tekst[0])
lista = lista + ["f", "g"]
print(lista)
print("Ilość: ", len(lista))

lista.append("f")
print(lista)

lista.append([1, 2, 3])
print(lista)

print(lista[7][1])

lista.insert(2, "f")
print(lista)
print("Ilość: ",lista.count(1))
print("Index: ", lista.index(2))
lista.remove("f")

lista2=[1, 20, 30, -5, 0]
print("Min: ", min(lista2))
print("Max: ", max(lista2))
lista2.sort()
print(lista2)
lista2.reverse()
print(lista2)
lista.clear()
print(lista)

