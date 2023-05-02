from egzP3btesty import runtests


def lufthansa(G):
    class Node:
        def __init__(self, value):
            self.value = value
            self.parent = self
            self.rank = 0

    def find(x):
        if x.parent != x:
            x.parent = find(x.parent)
        return x.parent

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank += 1

    def kruskal():
        nonlocal result
        flag = True
        for i in E:
            x = i[1]
            y = i[2]
            if find(tab[x]) != find(tab[y]):
                union(tab[x], tab[y])
                result += i[0]
            elif flag:
                result += i[0]
                flag = False

    num_of_flights = 0
    E = []
    for i in range(len(G)):
        for j in G[i]:
            if i < j[0]:
                E.append((j[1], i, j[0]))
            num_of_flights += j[1]
    num_of_flights //= 2
    E.sort(reverse=True)

    tab = [Node(i) for i in range(len(G))]
    result = 0
    kruskal()
    result = num_of_flights - result

    return result


runtests(lufthansa, all_tests=True)
