from zad6testy import runtests
from collections import deque

def longer( G, s, t ):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [-1 for _ in range(n)]

    def BFS():
        q = deque()

        visited[s] = True
        d[s] = 0
        q.append(s)

        while q and not visited[t]:
            v = q.popleft()
            for i in G[v]:
                if not visited[i]:
                    visited[i] = True
                    d[i] = d[v] + 1
                    q.append(i)

    def BFS_back():
        q = deque()

        visited[t] = True
        q.append(t)
        count = d[t]
        how_many = 1
        how_many_prev = 0

        while q:
            if how_many == how_many_prev == 1: return q[0], parent[q[0]]

            while q and d[q[0]] == count:
                v = q.popleft()
                for i in G[v]:
                    if not visited[i] and d[i] == count - 1:
                        visited[i] = True
                        parent[i] = v
                        q.append(i)

            how_many_prev = how_many
            how_many = len(q)
            count -= 1

        return None

    BFS()
    if not visited[t]:
        return None
    for i in range(n):
        visited[i] = False

    return BFS_back()

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
