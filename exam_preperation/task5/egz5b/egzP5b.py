from egzP5btesty import runtests 

def dfs(T):
    def dfs_visit(x):
        nonlocal time
        time += 1
        visited[x] = True
        d[x] = time
        low[x] = time
        for i in T[x]:
            if not visited[i]:
                parent[i] = x
                dfs_visit(i)
                low[x] = min(low[x], low[i])
            elif parent[x] != i:
                low[x] = min(low[x], d[i])

    n = len(T)
    d = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    low = [-1 for _ in range(n)]
    art_point = [False for _ in range(n)]
    time = 0
    #jako root ustawiamy pierwszy wierzchołek z wychodzącymi krawędziami
    for i in range(n):
        if T[i] != []:
            root = i
            break

    for i in range(n):
        if T[i] != [] and not visited[i]:
            dfs_visit(i)

    #sprawdzamy przypadek dla korzenia (czy jest punktem artykulacji)
    count = 0
    for i in range(n):
        if parent[i] == root:
            count += 1
            if count == 2:
                art_point[root] = True
                break

    for i in range(n):
        if parent[i] != -1 and low[i] >= d[parent[i]] and parent[i] != root:
            art_point[parent[i]] = True


    result = 0
    for i in range(n):
        if art_point[i]:
            result += 1
    return result


def koleje ( B ):
    n = len(B)
    B1 = [[B[i][0], B[i][1]] for i in range(n)]
    for i in range(n):
        if B1[i][0] > B1[i][1]:
            B1[i][0], B1[i][1] = B1[i][1], B1[i][0]

    B1.sort()
    B1.append([-1, -1])

    neighbours = [[] for _ in range(n)]
    for i in range(n):
        if B1[i] != B1[i+1]:
            neighbours[B1[i][0]].append(B1[i][1])
            neighbours[B1[i][1]].append(B1[i][0])

    return dfs(neighbours)


runtests(koleje, all_tests=True)
