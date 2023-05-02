from collections import deque
from zad7ktesty import runtests

def ogrodnik(T,D,Z,l):
    n = len(T)
    m = len(T[0])
    trees = len(D)
    water = [0 for _ in range(trees)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    def BFS(j, num,i=0):
        q = deque()
        q.append((i, j))
        visited[i][j] = 1

        while q:
            positions = q.popleft()
            x = positions[0]
            y = positions[1]
            water[num] += T[x][y]
            if x+1 < n and T[x+1][y] != 0 and visited[x+1][y] == 0:
                visited[x+1][y] = 1
                q.append((x+1, y))
            if y-1 >= 0 and T[x][y-1] != 0 and visited[x][y-1] == 0:
                visited[x][y-1] = 1
                q.append((x, y-1))
            if y+1 < m and T[x][y+1] != 0 and visited[x][y+1] == 0:
                visited[x][y+1] = 1
                q.append((x, y+1))

    for i in range(trees):
        BFS(D[i], i)

    tab = [[0 for _ in range(l+1)] for _ in range(trees + 1)]
    for i in range(1, trees + 1):
        for j in range(l+1):
            if j >= water[i-1]:
                tab[i][j] = max(tab[i-1][j], tab[i-1][j-water[i-1]] + Z[i-1])
            else:
                tab[i][j] = tab[i-1][j]
    return tab[trees][l]


runtests( ogrodnik, all_tests=True )
