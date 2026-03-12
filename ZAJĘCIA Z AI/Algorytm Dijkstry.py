import collections

# --- Definicja Grafu ---
graph = {
    'A': {'B': 2, 'D': 4},
    'B': {'C': 3, 'D': 3},
    'C': {'E': 2},
    'D': {'C': 3, 'E': 4},
    'E': {}
}


# --- 1. Funkcja do wyboru najtańszego, nieodwiedzonego wierzchołka ---
def wez_najtanszy_wierzcholek(slownik_kosztow, lista_ktore_byly):
    """Znajduje nieodwiedzony wierzchołek o najmniejszym aktualnym koszcie."""
    najmniejszy_koszt = float('inf')
    najtanszy_wierzcholek = None

    for wierzcholek in slownik_kosztow:
        koszt = slownik_kosztow[wierzcholek]
        # Sprawdzamy, czy wierzchołek nie był już przetworzony I ma najmniejszy koszt
        if koszt < najmniejszy_koszt and wierzcholek not in lista_ktore_byly:
            najmniejszy_koszt = koszt
            najtanszy_wierzcholek = wierzcholek

    return najtanszy_wierzcholek


# --- Inicjalizacja Danych ---
koszt = {}
poprzednik = {}

for name in graph:
    koszt[name] = float('inf')

wierzcholek_juz_byl = []
poczatkowy_wierzcholek = 'A'  # Startujemy z 'A'
koncowy_wierzcholek = 'E'

koszt[poczatkowy_wierzcholek] = 0
poprzednik[poczatkowy_wierzcholek] = None

# --- Główna Pętla Algorytmu Dijkstry ---
## 🏃‍♂️ Działanie Algorytmu

while poczatkowy_wierzcholek:

    # 1. Relaksacja krawędzi: Sprawdzanie sąsiadów bieżącego wierzchołka
    for somsiad in graph[poczatkowy_wierzcholek]:
        nowy_koszt = koszt[poczatkowy_wierzcholek] + graph[poczatkowy_wierzcholek][somsiad]

        # Jeśli nowa ścieżka do sąsiada jest tańsza niż dotychczasowa...
        if koszt[somsiad] > nowy_koszt:
            koszt[somsiad] = nowy_koszt
            poprzednik[somsiad] = poczatkowy_wierzcholek
    # 2. Bieżący wierzchołek został przetworzony
    wierzcholek_juz_byl.append(poczatkowy_wierzcholek)

    # 3. Wybór kolejnego wierzchołka do przetworzenia
    #   (o najmniejszym koszcie spośród nieodwiedzonych)
    poczatkowy_wierzcholek = wez_najtanszy_wierzcholek(koszt, wierzcholek_juz_byl)

# --- Wynik: Odtwarzanie Najkrótszej Ścieżki ---
## 🏆 Wyniki Końcowe

print("-" * 30)
print(f"Najkrótszy koszt z '{'A'}' do '{koncowy_wierzcholek}': {koszt[koncowy_wierzcholek]}")
print("-" * 30)

# Odtwarzanie ścieżki
if koszt[koncowy_wierzcholek] != float('inf'):
    sciezka = collections.deque()
    wierzcholek = koncowy_wierzcholek

    while wierzcholek is not None:
        sciezka.appendleft(wierzcholek)
        wierzcholek = poprzednik.get(wierzcholek)

    print("Najkrótsza ścieżka:")
    print(" -> ".join(sciezka))
else:
    print("Nie można dotrzeć do wierzchołka końcowego.")