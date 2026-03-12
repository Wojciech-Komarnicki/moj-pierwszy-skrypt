import math

class Punkt2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.odleglosc =  math.sqrt(x**2 + y**2)

    def __add__(self, drugi):
        return Punkt2D(self.x + drugi.x, self.y + drugi.y)
    def __sub__(self, drugi):
        return Punkt2D(self.x - drugi.x, self.y - drugi.y)
    def __mul__(self, drugi):
        return Punkt2D(self.x * drugi.x, self.y * drugi.y)
  #itp.
    def __lt__(self, drugi):
        return self.odleglosc < drugi.odleglosc

    def __le__(self, drugi):
        return self.odleglosc <= drugi.odleglosc
    def __eq__(self, drugi):
        return self.x == drugi.x and self.y == drugi.y
    def __len__(self):
        return int(round(self.odleglosc,0))
p1 = Punkt2D(1,2)
p2 = Punkt2D(3,4)
p3 = p1+p2
# Sposób nieczytelny
p4 = Punkt2D(p1.x + p2.x, p1.y + p2.y)
print(p3.x, p3.y)
print(p4.x, p4.y)

print(p1.odleglosc, p2.odleglosc,)
print(p1 < p2)
print(p1 > p2)
print(p1 == p2)

print(len(p1))