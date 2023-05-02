#Paweł Lamża
#############################################################################
#opis działania algorytmu:
#gdy k równe zero to zwracamy bo lista posortowana, poźniej sprawdzamy czy k nie jest większe niż n i w takim wypadku
#k zmieniamy na n-1 bo to oznacza że każdy element może być na dowolnym miejscu
#następnie adresy k+1 pierwszych node'ów z naszej listy zapisujemy w tablicy wielkości k+1
#która reprezentuje kopiec wielkości k+1 przy czym w korzeniu (tj. t[0]) mamy wartość najmniejszą tablicy
#następnie aż skończy nam się lista wykonujemy operacje, przepinania korzenia na koniec listy wynikowej, naprawienia kopca,
#a później wstawiania na miejsce korzenia w tablicy kolejego node'a z listy
#kiedy skończą nam się node'y w liście to pozostaje dopiąć do wynikowej listy wyrazy,
#znajdujące się w tablicy, od najmniejszego do największego
#na koniec opróżniamy tablicę oraz zwracamy head.next aby pozbyć się wcześniej utworzonego wartownika
#
#Jeśli chodzi o złożoność, to jest to Θ(n * log k), więc dla k = Θ(1) -> Θ(n),
#dla k = Θ(log n) -> Θ(n * log(log n)) oraz dla k = Θ(n) -> Θ(n * log n).


from zad1testy import Node, runtests

def left(i):
    return 2*i + 1
def right(i):
    return 2*i + 2
def parent(i):
    return (i - 1) // 2
def heapify(t, n, i):
    l = left(i)
    r = right(i)
    min_ind = i
    if l < n and t[l].val < t[min_ind].val:
        min_ind = l
    if r < n and t[r].val < t[min_ind].val:
        min_ind = r
    if min_ind != i:
        t[min_ind], t[i] = t[i], t[min_ind]
        if 2*min_ind + 1 < n:
            heapify(t,n,min_ind)
def build_heap(t):
    n = len(t)
    for i in range(parent(n - 1), -1, -1):
        heapify(t, n, i)


def SortH(p,k):
    if k == 0:
        return p

    pp = p
    count = k
    while pp is not None and count >= 0:
        count -= 1
        pp = pp.next
    if count >= 0:
        k -= (count + 1)

    head = Node()
    t = [0 for _ in range(k+1)]
    for i in range(k+1):
        if p is None:
            k = i
            break
        t[i] = p
        p = p.next
    build_heap(t)
    q = head
    while p is not None:
        q.next = t[0]
        t[0] = p
        heapify(t,k+1,0)
        p = p.next
        q = q.next
    for i in range(k, -1, -1):
        q.next = t[0]
        q = q.next
        t[0] = t[i]
        heapify(t,i,0)
    q.next = None
    t *= 0
    return head.next
runtests( SortH )
