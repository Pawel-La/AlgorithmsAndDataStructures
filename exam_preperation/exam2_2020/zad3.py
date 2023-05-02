from zad3testy import runtests
from collections import deque

    
def tasks(T):
    n = len(T)
    visited = [False for _ in range(n)]
    result = deque()
    def dfs_visit(u):
        visited[u] = True
        for v in range(n):
            if T[u][v] == 1 and not visited[v]:
                dfs_visit(v)

        result.appendleft(u)


    def dfs():
        for i in range(n):
            if not visited[i]:
                dfs_visit(i)
    dfs()
    return result

runtests( tasks )
