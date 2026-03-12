def dzielenie(x,y):
    assert not y == 0
    if y ==0:
        raise ZeroDivisionError("Dzielenie przez 0")
    print(x/y)
try:
    dzielenie(2,0)
except Exception as e:
    print(e)