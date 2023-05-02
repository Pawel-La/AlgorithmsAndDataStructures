from zad3ktesty import runtests

def ksuma(T, k):
    n = len(T)
    tab = [0 for _ in range(n)]
    for i in range(k):
        tab[i] = T[i]
    for i in range(k, n):
        _min = 10000000
        for j in range(k):
            _min = min(_min, tab[i-j-1])
        tab[i] = _min + T[i]
    _min = tab[n-1]
    for i in range(n-1, n-k-1, -1):
        _min = min(_min, tab[i])
    return _min

runtests(ksuma)
