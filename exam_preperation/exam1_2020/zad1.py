from zad1testy import runtests
from queue import PriorityQueue


def islands(G, A, B):
    n = len(G)
    tab = [[0 for _ in range(3*n)] for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            row = 3 * i
            col = 3 * j
            if G[i][j] == 1:
                x = 0
            elif G[i][j] == 5:
                x = 1
            else:
                x = 2
            col += x
            for k in range(3):
                if k != x:
                    tab[row + k][col] = G[i][j]

    d = [float('inf') for _ in range(3*n)]
    visited = [False for _ in range(3*n)]

    def dijkstra():
        q = PriorityQueue()
        d[3 * A] = 0
        d[3 * A + 1] = 0
        d[3 * A + 2] = 0
        q.put((0, 3 * A))
        q.put((0, 3 * A + 1))
        q.put((0, 3 * A + 2))

        while not q.empty():
            distance, u = q.get()
            if visited[u]:
                continue
            for v in range(3 * n):
                if tab[u][v] != 0 and not visited[v]:
                    if d[v] > d[u] + tab[u][v]:
                        d[v] = d[u] + tab[u][v]
                        q.put((d[v], v))
            visited[u] = True
            if u // 3 == B:
                break
        return min(d[3*B], d[3*B + 1], d[3*B + 2])

    return dijkstra()


#G = [[0,5,0,1],[5,0,1,1],[0,1,0,5],[1,1,5,0]]
#print(islands(G, 2, 0))
runtests( islands )
