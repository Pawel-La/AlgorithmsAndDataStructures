#Weronika Klatka
#Sortuje najpierw rosnąco po początkach przedziału i zliczam ile jest przedziałów
#mających dany taki sam początek, wyznaczam przedziały potencialnie największe bo będące
#najdłuższymi przedziałami dla danego początku
#Potem sortuje po końcach malejąco i znowu zliczam ile jest przedziałów mających dany taki sam koniec
#wtedy znowu wyznaczyliśmy potencjalnie największe przedziały te co wcześniej
#Teraz wystarczy tylko zliczyć długość każdego z potencjanych przedziałów
#i dostajemy najdłuższy przedział
#Jeśli chodzi o złożoność to jest to O(nlogn)

from zad2testy import runtests


def quicksort1(tab, left, right):
    i = left
    j = right
    if left >= right:
        return
    x = tab[(left + right) // 2]
    while True:
        while x[0] < tab[j][0] or (x[0] == tab[j][0] and x[1] > tab[j][1]):
            j -= 1
        while x[0] > tab[i][0] or (x[0] == tab[i][0] and x[1] < tab[i][1]):
            i += 1
        if i <= j:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
            j -= 1
        else:
            break
    if j > left:
        quicksort1(tab, left, j)
    if i < right:
        quicksort1(tab, i, right)


def quicksort2(tab, left, right):
    i = left
    j = right
    if left >= right:
        return
    x = tab[(left + right) // 2]
    while True:
        while x[1] > tab[j][1] or (x[1] == tab[j][1] and x[0] < tab[j][0]):
            j -= 1
        while x[1] < tab[i][1] or (x[1] == tab[i][1] and x[0] > tab[i][0]):
            i += 1
        if i <= j:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
            j -= 1
        else:
            break
    if j > left:
        quicksort2(tab, left, j)
    if i < right:
        quicksort2(tab, i, right)


def depth(L):
    n = len(L)
    quicksort1(L, 0, n-1)

    x = L[0][0]
    y = L[0][1]
    best_count = 0
    for i in range(1, n):
        if x <= L[i][0] and L[i][1] <= y:
            best_count += 1

    t1 = []
    count = 0
    for i in range(1, n):
        if x <= L[i][0] and L[i][1] <= y:
            count += 1
        else:
            t1.append(count)
            count = 0
            x, y = L[i][0], L[i][1]
    t1.append(count)
    m = len(t1)

    quicksort2(L, 0, n-1)
    t2 = [0 for _ in range(m)]
    x = L[0][0]
    y = L[0][1]
    count = 0
    ind = m-1
    for i in range(1, n):
        if x <= L[i][0] and L[i][1] <= y:
            count += 1
        else:
            t2[ind] = count
            ind -= 1
            count = 0
            x, y = L[i][0], L[i][1]
    t2[ind] = count

    max_try = best_count
    for i in range(m-1):
        max_try = max_try - t1[i] + t2[i+1]
        best_count = max(best_count, max_try)

    return best_count


runtests(depth)
