from egzP7atesty import runtests
from queue import Queue


def akademik(T):
    def bfs():
        q = Queue()
        q.put(2*n)
        visited[2*n] = True
        while not q.empty() and not visited[2*n + 1]:
            u = q.get()
            for i in range(2*n + 2):
                cap = capacity[u][i] - flow[u][i]
                if cap > 0 and not visited[i]:
                    parent[i] = u
                    visited[i] = True
                    q.put(i)

    n = len(T)
    flow = [[0 for _ in range(2 * n + 2)] for _ in range(2 * n + 2)]        #O(n^2)
    capacity = [[0 for _ in range(2 * n + 2)] for _ in range(2 * n + 2)]    #O(n^2)
    satisfied = 0
    for i in range(n):  #O(n)
        for j in T[i]:  #O(1)
            if j is None:
                continue
            capacity[i][n + j] = 1
        capacity[2*n][i] = 1
        capacity[n+i][2*n + 1] = 1
        if T[i] == (None, None, None):
            satisfied += 1

    visited = [False for _ in range(2 * n + 2)]     #O(n)
    parent = [None for _ in range(2 * n + 2)]       #O(n)

    while True:     #O(n)
        for i in range(2 * n + 2):     #O(n)
            visited[i] = False
            parent[i] = None
        bfs()   #O(n^2)
        #we didnt reach end point during bfs so we end algorithm
        if not visited[2*n + 1]:
            break

        # x = 2 * n + 1
        # cap = float('inf')
        # while x is not None and parent[x] is not None:
        #     cap = min(cap, capacity[parent[x]][x] - float[parent[x]][x])
        #     x = parent[x]
        x = 2*n + 1
        cap = 1
        while x is not None and parent[x] is not None:  #O(n)
            flow[parent[x]][x] += cap
            flow[x][parent[x]] -= cap
            x = parent[x]

    for i in range(n):
        satisfied += flow[2*n][i]
    result = n - satisfied

    return result

runtests(akademik, all_tests=True)
