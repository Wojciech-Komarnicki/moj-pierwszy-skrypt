import collections
import queue

graf = {
    1: [(2, 1), (3, 1)],
    2: [(1, 1), (5, 7)],
    3: [(1, 1), (4, 2)],
    4: [(3, 2), (6, 1)],
    5: [(2, 7), (6, 3), (8, 2)],
    6: [(4, 1), (5, 3), (7, 5), (8, 6)],
    7: [(6, 5)],
    8: [(5, 2), (6, 6)]
}


def znajdz_najkrotsza_sciezke(G, poczatek, koniec):
    dystans = collections.defaultdict(lambda: float('inf'))
    dystans[poczatek] = 0
    poprzednik = {}

    kp = queue.PriorityQueue()
    kp.put((0, poczatek))

    while not kp.empty():
        d_u, u = kp.get()

        if d_u > dystans[u]:
            continue

        if u == koniec:
            break

        for v, waga in G[u]:
            nowy_dystans = dystans[u] + waga

            if nowy_dystans < dystans[v]:
                dystans[v] = nowy_dystans
                poprzednik[v] = u
                kp.put((nowy_dystans, v))

    return dystans, poprzednik


def odtworz_sciezke(poprzednik, poczatek, koniec):
    sciezka = collections.deque()
    w = koniec

    while w is not None and w in poprzednik:
        sciezka.appendleft(w)
        w = poprzednik[w]

    if w == poczatek:
        sciezka.appendleft(poczatek)
        return list(sciezka)
    else:
        return []


START = 1
KONIEC = 8

odl, poprz = znajdz_najkrotsza_sciezke(graf, START, KONIEC)

dlugosc_min = odl[KONIEC]
sciezka_min = odtworz_sciezke(poprz, START, KONIEC)

print("-------------------")
print("Zadanie 3 - Wynik")
print("-------------------")
print(f"Najkrótsza ścieżka z wierzchołka {START} do wierzchołka {KONIEC}: {sciezka_min}")
print(f"Minimalna długość: {dlugosc_min}")