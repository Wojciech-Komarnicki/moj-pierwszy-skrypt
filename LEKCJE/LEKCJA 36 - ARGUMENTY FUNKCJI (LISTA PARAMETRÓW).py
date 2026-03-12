def funkcja(arg1, arg2="World", *args,**kwargs):
    print(arg1)
    print(arg2)

    for x in args:
        print(x)
    print(kwargs)

    for x in kwargs.values():
        print(x)
funkcja("hello", "twoja", "Stara", autor="seba",rok=1992)