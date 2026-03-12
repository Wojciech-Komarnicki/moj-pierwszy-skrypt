class Czlowiek:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self, powitanie = "Cześć, "):
        return powitanie + "mam na imię "+self.imie +" "+ str(self.wiek) + " lat"

obiekt = Czlowiek("Sebastiawan", 24)
print(obiekt.przedstaw_sie("Witam, "))

obiekt2=Czlowiek("Wojtek", 21)
obiekt2.imie = "Wojtek"
print(obiekt2.przedstaw_sie())

print(obiekt.przedstaw_sie())
