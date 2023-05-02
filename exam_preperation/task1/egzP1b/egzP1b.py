from egzP1btesty import runtests
from queue import PriorityQueue

def change_to_neightbours_list(G):
    n = 0
    for i in G:
        n = max(n, i[1])
    result = [[] for _ in range(n+1)]
    for i in G:
        result[i[0]].append((i[1], i[2]))
        result[i[1]].append((i[0], i[2]))
    return result, n+1


def turysta(G, s, e):
    G, n = change_to_neightbours_list(G)

    e_neightbours = [-1 for _ in range(n)]
    for i in G[e]:
        e_neightbours[i[0]] = i[1]

    dist = [[float('inf'), float('inf'), float('inf'), float('inf')] for _ in range(n)]
    q = PriorityQueue()

    for i, j in G[s]:
        q.put((j, i, 1, s))

    while not q.empty():
        point = q.get()
        value = point[0]
        point_num = point[1]
        num_of_visited_points = point[2]
        parent = point[3]

        if point_num == e:
            return value

        if dist[point_num][num_of_visited_points] < value:
            continue
        dist[point_num][num_of_visited_points] = value

        if num_of_visited_points < 3:
            for neighbour, x in G[point_num]:
                if neighbour != s and neighbour != parent and neighbour != e:
                    q.put((value + x, neighbour, num_of_visited_points + 1, point_num))
        elif e_neightbours[point_num] != -1:
            q.put((value + e_neightbours[point_num], e, 0, 0))


runtests(turysta)
