from egzP7atesty import runtests


def akademik(T):
    def dfs_visit(i):
        visited[i] = True
        for j in neighbours[i]:
            if visited[2*n + 1]:
                return
            cap = j[1] - j[2]
            #cap = capacity[i][j] - flow[i][j]
            if cap > 0 and not visited[j[0]]:
                parent[j[0]] = i
                dfs_visit(j[0])


        # for j in range(2*n + 2):
        #     if visited[2*n + 1]:
        #         return
        #     cap = capacity[i][j] - flow[i][j]
        #     if cap > 0 and not visited[j]:
        #         parent[j] = i
        #         dfs_visit(j)

    n = len(T)
    #flow = [[0 for _ in range(2*n + 2)] for _ in range(2*n + 2)]
    #capacity = [[0 for _ in range(2*n + 2)] for _ in range(2*n + 2)]
    #[who, capacity, flow]
    neighbours = [[] for _ in range(2*n + 2)]
    count = 0

    for i in range(n):
        for j in T[i]:
            if j is not None:
                neighbours[i].append([n + j, 1, 0])
                #capacity[i][n + j] = 1
        neighbours[2 * n].append([i, 1, 0])
        neighbours[n + i].append([2*n + 1, 1, 0])
        #capacity[2 * n][i] = 1
        #capacity[n + i][2*n + 1] = 1
        if T[i] == (None, None, None):
            count += 1

    visited = [False for _ in range(2 * n + 2)]
    parent = [None for _ in range(2 * n + 2)]
    result = 0
    while True:
        for i in range(2*n + 2):
            visited[i] = False
            parent[i] = None

        dfs_visit(2*n)
        if parent[2*n + 1] is None:
            break

        x = 2 * n + 1
        add = 1

        while parent[x] is not None:
            result += 1
            for i in range(len(neighbours[x])):
                if neighbours[x][i][0] == parent[x]:
                    neighbours[x][i][2] += 1
            for i in range(len(neighbours[parent[x]])):
                if neighbours[parent[x]][i][0] == x:
                    neighbours[parent[x]][i][2] -= 1
            x = parent[x]

    # result = 0
    # for i in range(n):
    #     result += flow[2*n][i]

    result = n - result - count

    return result


runtests(akademik, all_tests=True)
