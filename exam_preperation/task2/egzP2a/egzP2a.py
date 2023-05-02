from egzP2atesty import runtests 


def zdjecie(T, m, k):
    n = len(T)

    def partition(A, p, r):
        x = A[r][1]
        i = p - 1
        for j in range(p, r):
            if A[j][1] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        return i + 1

    def quick_sort(A, p, r):
        if p < r:
            q = partition(A, p, r)
            quick_sort(A, p, q-1)
            quick_sort(A, q+1, r)

    def select(A, p, l, r):
        if p == r:
            return A[p]
        if p < r:
            q = partition(A, p, r)
            if q == l:
                return A[q]
            elif q < l:
                return select(A, q+1, l, r)
            else:
                return select(A, p, l, q-1)

    count = k - 1
    T3 = T.copy()
    T2 = []
    for i in range(m):
        select(T3, 0, count, len(T3) - 1)
        count += 1
        for j in range(count):
            T2.append(T3[j])
        T3 = T3[count:]
    for i in range(n):
        T[i] = T2[i]

    top = k + m - 1
    how_many = [0 for _ in range(top)]
    for i in range(top):
        how_many[i] = min(m, m + k - i - 1)

    rows = [0 for _ in range(m)]
    count = 0
    for i in range(m):
        rows[m - 1 - i] = count
        count += k
        k += 1

    indexes = [0 for _ in range(n)]
    x = 0
    for i in range(top):
        for j in range(how_many[i]):
            indexes[x] = rows[j]
            rows[j] += 1
            x += 1

    for i in range(n):
        T2[i] = T[indexes[i]]
    for i in range(n):
        T[i] = T2[i]

    return None


runtests(zdjecie, all_tests=False)
