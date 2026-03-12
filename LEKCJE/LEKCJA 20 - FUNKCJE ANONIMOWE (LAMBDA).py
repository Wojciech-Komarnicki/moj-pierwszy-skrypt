def funkcja(f,liczba):
    return f(liczba)



print(funkcja(lambda x: x*x,3))

def kwadrat(x):
    return x*x
print(kwadrat(4))

wyn = (lambda x: x*x)(6)
print(wyn)
#lub
wyn2 = lambda x: x*x
print(wyn2(6))

lam = lambda x,y: x*y
print(lam(2,22))
