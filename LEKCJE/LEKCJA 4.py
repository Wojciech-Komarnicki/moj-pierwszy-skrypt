wiek = 12
kasa = 4
cena_biletu=35
dozwolony_wiek=18
wiek_znizka = 12
cena_znizka = 20

# if wiek >= dozwolony_wiek:
#     if kasa >= cena_biletu:
#         print("Możesz wejść")
# else:
#     print("Sory memory. Won")
#
#
# if wiek >= dozwolony_wiek and kasa >= cena_biletu:
#     print("Możesz wejść")
# else:
#     print("Sory memory. Won")
#
#
# if wiek>wiek_znizka:
#     print(f"Wchodzisz i płacisz: {cena_biletu}")
# else:
#     print(f"Wchodzisz i płacisz {cena_znizka}")


if wiek <= wiek_znizka or kasa >= cena_biletu:
    print("Możesz wejść")
else:
    print("Konwersja")
