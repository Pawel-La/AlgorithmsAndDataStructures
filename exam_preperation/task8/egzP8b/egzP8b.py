from egzP8btesty import runtests


def robot(G, P):
    def transform_graph(x):
        transformed_x = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            transformed_x[i][i] = 0
        for i in range(n):
            for j in x[i]:
                transformed_x[i][j[0]] = j[1]
        return transformed_x

    n = len(G)
    G = transform_graph(G)
    for k in range(n):
        for u in range(n):
            for v in range(n):
                G[u][v] = min(G[u][v], G[u][k] + G[k][v])

    result = 0
    for i in range(len(P) - 1):
        result += G[P[i]][P[i+1]]

    return result

    
runtests(robot, all_tests=True)
