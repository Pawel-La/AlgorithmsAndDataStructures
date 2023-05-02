#Paweł Lamża
#Pomysłem na rozwiązanie jest dodawanie tych plam ropy które mijamy do kolejki i następnie wyciąganie z tej kolejki
#najlepszej plamy (lokalnie) wtedy kiedy nasze paliwo w danym momencie wyniesie 0. Wyciąganie z kolejki jest równoznaczne
#z zatrzymywaniem się na danej plamie(danym indeksie) a co za tym idzie dodawanie danego indeksu do tablicy rozwiązań
#na końcu musimy jeszcze posortować tablicę indeksów
from queue import PriorityQueue
from zad5testy import runtests

def plan(T):
    n = len(T)
    q = PriorityQueue()
    sol = []
    fuel = 0
    for i in range(n-1):
        if T[i]:
            #dodajemy minus przed T[i] w kolejce priorytetowej aby wartości paliwa były posortowane rosnąco po pominięciu znaku
            q.put((-T[i], i))
        if not fuel:
            item = q.get()
            #zmieniamy znak przy wartości paliwa na dodatnią poprzez pomnożenie przez -1
            fuel = -item[0]
            sol.append(item[1])
        fuel -= 1
    return sorted(sol)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )
