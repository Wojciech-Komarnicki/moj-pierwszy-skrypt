class Czlowiek:
    def __init__(self, imie):
        self.imie = imie

    def przedstaw_sie(self):
        print("Nazywam się "+self.imie)

    @classmethod
    def nowy_Czlowiek(cls, imie):
        return cls(imie)

czlowiek1 = Czlowiek.nowy_Czlowiek("Seba")
czlowiek1.przedstaw_sie()
