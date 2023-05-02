from zad3testy import runtests


def insertion_sort(t):
    n = len(t)
    for i in range(0, n - 1):
        if t[i] > t[i + 1]:
            j = i + 1
            while j and t[j - 1] > t[j]:
                t[j], t[j - 1] = t[j - 1], t[j]
                j -= 1
    return


def SortTab(T,P):
    N = len(T)
    tab = [0 for _ in range(N)]
    for i in P:
        begin = i[0]
        end = i[1]
        diff = end - begin
        chance = i[2]
        if not diff:
            tab[begin - 1] += chance
        else:
            lol = chance / diff
            tab[begin - 1] += lol
            tab[end   - 1] -= lol
    for i in range(1, N):
        tab[i] += tab[i - 1]
    for i in range(1, N):
        tab[i] += tab[i - 1]

    buckets = [[] for _ in range(N//10)]

    for el in T:
        x = int(el)
        rest = x % 1
        if x == 1:
            ind = int(tab[0] * rest * N)
        else:
            ind = int((tab[x - 2] + ((tab[x - 1] - tab[x - 2]) * rest)) * N)
            ind = min(ind, N - 1)
        buckets[ind//10].append(el)

    for i in buckets:
        if len(i) > 0:
            insertion_sort(i)

    k = 0
    for i in range(N//10):
        for j in range(len(buckets[i])):
            T[k] = buckets[i][j]
            k += 1

    return T


runtests( SortTab )

