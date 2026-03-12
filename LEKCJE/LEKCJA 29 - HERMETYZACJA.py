class Test:
    lista = []
    def dodaj(self, arg):
        self.lista.append(arg)
    def zdejmij(self):
        if len(self.lista) > 0:
            return self.lista.pop(len(self.lista) - 1)
        else:
            return None
obj = Test()
obj.dodaj("A")
obj.dodaj("B")
print(obj.zdejmij())