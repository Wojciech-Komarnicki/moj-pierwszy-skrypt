class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):

    def voice(self):
        print("How how")

class Wolf(Dog):
    def dajvoice(self):
        print("Jestem wilkiem, ")
        super().voice()


class Cat(Animal):
    def getvoice(self):
        print("Meow meow")

dog = Dog("Łatek", 10)
print(dog.name)
print(dog.age)
dog.voice()

cat = Cat("Gacuś", 5)
cat.getvoice()

wilk = Wolf("Grozny", 10)
wilk.dajvoice()
