class Test:
    def __del__(self):
        print("Bye class")

obj = Test()
obj2 = obj
del obj

print("Siema")
