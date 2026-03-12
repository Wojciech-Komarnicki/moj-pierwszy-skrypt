class KontoBankowe:
    __stan = 0
    @property
    def stan_konta(self):
        return self.__stan
    @stan_konta.getter
    def stan_konta(self):
        return "Stan konta: " + str(self.__stan)+" zł"

    @stan_konta.setter
    def stan_konta(self, wartosc):
        self.__stan += wartosc

konto = KontoBankowe()
print(konto.stan_konta)

konto.stan_konta = 50
print(konto.stan_konta)