from zad4testy import runtests


#quicksort indeksow tablicy T, pod wzgledem koncow budynkow
def quicksort(tab, t, l, r):
    if l >= r:
        return
    i, j = l, r
    pivot = t[tab[(l+r) // 2]][2]
    while i <= j:
        while t[tab[i]][2] < pivot:
            i += 1
        while t[tab[j]][2] > pivot:
            j -= 1
        if i <= j:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
            j -= 1
    if l < j:
        quicksort(tab, t, l, j)
    if i < r:
        quicksort(tab, t, i, r)


def select_buildings(T, p):
    n = len(T)
    tab = [i for i in range(n)]
    quicksort(tab, T, 0, n-1)
    #tab - indeksy tablicy T posortowane rosnaco pod wzgledem koncow przedzialow
    memo = [[-1 for _ in range(p+1)] for _ in range(n+1)]

    def selecting(x, v=0, i=0, end=-1):
        if x < 0 or (memo[end+1][x] != -1 and v < memo[end+1][x]):
            return [], -1
        if i == n or x == 0:
            #for i in range(0, x+1):
            memo[end+1][x] = max(memo[end+1][x], v)
            return [], v

        if end == -1 or T[tab[i]][1] > T[tab[end]][2]:

            #places =      h      *      (b       -       a)
            places = T[tab[i]][0] * (T[tab[i]][2] - T[tab[i]][1])

            t1 = selecting(x, v, i + 1, end)
            t2 = selecting(x - T[tab[i]][3], v + places, i + 1, i)
            if t1[1] > t2[1]:
                return t1[0], t1[1]
            t2[0].append(tab[i])
            return t2[0], t2[1]

        t1 = selecting(x, v, i + 1, end)
        return t1[0], t1[1]

    res = selecting(p)
    return res[0]


runtests( select_buildings )
