def potegi_dwojki():
    i = 0
    while i <10:
        yield 2**i
        i+=1

# for i in potegi_dwojki():
#     print(i)

def generator_liczb_parzystych(start, koniec):
    while start <= koniec:
        if start % 2 == 0:
            yield start
        start +=1
#print(list(generator_liczb_parzystych(0, 10)))

def generator_statusu_pomiaru(dane_temperatury: list):
    for temperatury in dane_temperatury:
        if temperatury >26:
            yield f"Temperatura została przekroczona i w indeksie nr: {dane_temperatury.temp[temperatury]} wynosi: {temperatury}"
print(list(generator_statusu_pomiaru([26, 23, 24.3, 29.3])))


