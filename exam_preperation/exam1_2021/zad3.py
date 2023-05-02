from zad3testy import runtests


def k_intersect(A, k):
    n = len(A)
    t1 = []
    t2 = []
    t = [-1]

    # O(n) * O(1) = O(n)
    for i in A:
        t1.append(i[0])
        t2.append(i[1])
        t.append(i[0])
        t.append(i[1])
    # O(nlogn)
    t1.sort()
    t2.sort()
    t.sort()
    counter = [0 for _ in range(2*n)]

    i, j, k = 0, 0, 0
    count = 0
    while i < n and j < n:
        while i < n and t1[i] == t[k]:
            count += 1








runtests(k_intersect)
