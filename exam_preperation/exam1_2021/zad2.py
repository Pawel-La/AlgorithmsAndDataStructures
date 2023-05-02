from zad2testy import runtests
from queue import PriorityQueue


def robot(L, A, B):
    def action(p, t):
        q.put((t, p))
        #if L[p[0]][p[1]] == ' ' and T[p[0]][p[1]][p[2]][p[3]] == float('inf'):


    def right(p, t):
        time = t
        q = p.copy()
        q[2] += 1
        q[2] %= 4
        q[3] = 0
        time += 45
        action(q, time)

    def left(p, t):
        time = t
        q = p.copy()
        q[2] += 3
        q[2] %= 4
        q[3] = 0
        time += 45
        action(q, time)

    def ddirection(x):
        if x == 0:
            return 0, 1
        if x == 1:
            return 1, 0
        if x == 2:
            return 0, -1
        if x == 3:
            return -1, 0

    def ttimer(p):
        if p[3] == 0:
            return 60
        elif p[3] == 1:
            return 40
        else:
            return 30

    def straight(p, t):
        q = p.copy()
        time = t + timer(q)
        direct = direction(q[2])
        q[0] += direct[0]
        q[1] += direct[1]
        q[3] += 1
        q[3] = min(q[3], 2)
        action(q, time)

    def move():
        t, p = q.get()
        T[p[0]][p[1]][p[2]][p[3]] = t
        if p[0] == B[1] and p[1] == B[0]:
            return True
        action([p[0], p[1], (p[2] + 1) % 4, 0], t + 45)
        action([p[0], p[1], (p[2] + 3) % 4, 0], t + 45)
        action([p[0] + direction[p[2]][0], p[1] + direction[p[2]][1], p[2], min(p[3] + 1, 2)], t + timer(p))
        #right(p, t)
        #left(p, t)
        #straight(p, t)

    n = len(L)
    m = len(L[0])
    T = [[[[float('inf') for _ in range(3)] for _ in range(4)] for _ in range(m)] for _ in range(n)]
    direction = [(0,1), (1,0), (0,-1), (-1,0)]
    timer = [60,40,30]
    place = [A[1], A[0], 0, 0]
    time = 0
    q = PriorityQueue()
    q.put((time, place))
    while not q.empty():
        t, p = q.get()
        if L[p[0]][p[1]] != ' ' or T[p[0]][p[1]][p[2]][p[3]] != float('inf'):
            continue
        T[p[0]][p[1]][p[2]][p[3]] = t
        if p[0] == B[1] and p[1] == B[0]:
            break
        action([p[0], p[1], (p[2] + 1) % 4, 0], t + 45)
        action([p[0], p[1], (p[2] + 3) % 4, 0], t + 45)
        action([p[0] + direction[p[2]][0], p[1] + direction[p[2]][1], p[2], min(p[3] + 1, 2)], t + timer[p[3]])

    result = min(min(T[B[1]][B[0]]))

    if result == float('inf'):
        return None

    return result


runtests(robot)
