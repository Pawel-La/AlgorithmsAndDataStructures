from zad1testy import runtests
from queue import PriorityQueue
def intuse(I, x, y):
    T = [(I[i][0], I[i][1], i) for i in range(len(I))]
    T.sort()
    #0 - not useful, 1 - useful only from start [x,z] z != y, 2 - useful
    useful = [0 for _ in range(len(I))]
    q = PriorityQueue()
    q.put(x)

    idx = 0
    prev = -1

    while not q.empty():
        a = q.get()
        if a == prev:
            continue
        prev = a

        while idx < len(I) and T[idx][0] <= a:
            if T[idx][0] == a and T[idx][1] <= y:
                useful[T[idx][2]] = 1
                q.put(T[idx][1])
            idx += 1

    T1 = [(I[i][1], I[i][0], i) for i in range(len(I))]
    T1.sort(reverse=True)
    q1 = PriorityQueue()
    q1.put(-y)

    idx = 0
    prev = -1

    while not q1.empty():
        a = -q1.get()
        if a == prev:
            continue
        prev = a

        while idx < len(I) and T1[idx][0] >= a:
            if T1[idx][0] == a and T1[idx][1] >= x:
                if useful[T1[idx][2]] == 1:
                    useful[T1[idx][2]] = 2
                    q1.put(-T1[idx][1])
            idx += 1

    res = []
    for i in range(len(I)):
        if useful[i] == 2:
            res.append(i)
    return res

runtests(intuse)
