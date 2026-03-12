import re

wzor = r"banan"
tekst = r"dasdbanangruszkabananjabłkobanandas"

print(re.match(wzor, tekst))

if re.match(r".*"+wzor+r".*", tekst):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.search(wzor, tekst):
    print("Dopasowano")
else:
    print("Nie dopasowano")

wzor1 = r"^\d{2}-\d{3}$"
tekst1 = "66-415"
if re.findall(wzor1, tekst1):
    print("Dopasowano")
else:
    print("Nie dopasowano")

wzor2 = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
tekst2 = "dasndkja@danskj.com"
if re.fullmatch(wzor2, tekst2):
    print("Dopasowano")
else:
    print("Nie dopasowano")

print(re.findall(wzor1, tekst1))
dopasowanie = re.search(wzor, tekst)
if dopasowanie:
    print(dopasowanie.group())
    print(dopasowanie.start())
    print(dopasowanie.end())
    print(dopasowanie.span()) # start i end

tekst2 = re.sub(wzor, r"lol", tekst) 
print(tekst2)