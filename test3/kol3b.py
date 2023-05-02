#Paweł Lamża
#zlozonosc O(n^2)
#tworzymy macierz połaczen nxn do ktorej wpisujemy wage polaczenia z u do v (bezposredniego)
#tzn. ze kiedy nie ma bezposredniej sciezki miedzy u i v to dajemy w odpowiednie pole macierzy wartosc kosztu
#uzycia szybowca z jednego miasta do drugiego
#nastepnie zaczynamy od wierzcholka s i wpisujemy w nim wartosc 0 i relaksujemy wszystkie pozostałe wierzcholki
#(troche jak w algorytmie Dijkstry) o ile nie byly rozwazone wczesniej.
#w ten sposob z kazdego wierzcholka wykonujemy O(n) operacji dla kazdego wierzcholka tylko raz
#bo pomimo tego iz wierzcholek moze sie znalezc w kolejce n razy to jesli napotkamy go po raz drugi to pominiemy go
#poniewaz zostal juz rozwazony a zatem n * n operacji czyli zlozonosc O(n^2)

from queue import PriorityQueue
from kol3btesty import runtests

def convert_to_matrix(G, n, A):
    tab = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            tab[i][j[0]] = j[1]
        for k in range(n):
            cost = A[i] + A[k]
            if (tab[i][k] == 0 or cost < tab[i][k]) and i != k:
                tab[i][k] = cost
    return tab

def airports( G, A, s, t ):
    n = len(G)
    G = convert_to_matrix(G, n, A)
    #done - tablica przechowujaca informacje o przetworzeniu lotnisk
    done = [False for _ in range(n)]
    #d - tablica "distances" - najtanszej drogi do kazdego miejsca zaczynajac w s
    d = [-1 for _ in range(n)]
    q = PriorityQueue()
    q.put((0, s))
    d[s] = 0

    while not q.empty() and not done[t]:
        # cost = u[0]
        # aeropuerto = u[1]
        u = q.get()
        j = u[1]
        if done[j]:
            continue
        for i in range(n):
            if i != j and (d[i] == -1 or d[i] > d[j] + G[j][i]):
                d[i] = d[j] + G[j][i]
                q.put((d[i], i))

        done[j] = True

    return d[t]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )
