import math
from zad8testy import runtests

def highway( A ):
    def days(x1, x2, y1, y2):
        return math.ceil(math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)))

    def convert(G):
        E = []
        for i in range(len(G)):
            for j in range(i + 1, len(G)):
                x1, y1 = G[i][0], G[i][1]
                x2, y2 = G[j][0], G[j][1]
                E.append((days(x1, x2, y1, y2), i, j))
        return sorted(E)

    def make_sets(n):
        global p, r
        p = [i for i in range(n)]
        r = [0 for _ in range(n)]

    def find(x):
        global p, r
        if x != p[x]:
            p[x] = find(p[x])
        return p[x]

    def union(x, y):
        global p, r
        x = find(x)
        y = find(y)
        if x == y:
            return
        if r[x] > r[y]:
            p[y] = x
        else:
            p[x] = y
            if r[x] == r[y]:
                r[y] += 1

    def kruskal(G):
        m = len(G)
        count_min = 100000000
        E = convert(G)
        n = len(E)

        for i in range(n-m+2):
            _min = E[i][0]
            make_sets(m)
            _edges = m-1
            _max = 0
            if E[i+m-2][0] - _min < count_min:
                for j in range(i, n):
                    w, x, y = E[j]
                    if find(x) != find(y):
                        _last = j
                        union(x, y)
                        _max = E[j][0]
                        _edges -= 1
                        if _max - _min > count_min:
                            break
                        if not _edges:
                            break
                if not _edges:
                    count_min = min(count_min, _max - _min)
        return count_min

    return kruskal(A)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )
