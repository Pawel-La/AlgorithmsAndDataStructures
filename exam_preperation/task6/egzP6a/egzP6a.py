from egzP6atesty import runtests 


# def google(H, s):
#     def compare(x, y):
#         if x[0] > y[0]:
#             return True
#         if x[0] < y[0]:
#             return False
#         return x[1] >= y[1]
#
#     def partition(p, r):
#         x = H[r]
#         i = p - 1
#         for j in range(p, r):
#             if compare(x, H[j]):
#                 i += 1
#                 H[i], H[j] = H[j], H[i]
#         H[i+1], H[r] = H[r], H[i+1]
#         return i + 1
#
#     def quicksort(p, r):
#         if p < r:
#             q = partition(p, r)
#             quicksort(p, q-1)
#             quicksort(q+1, r)
#
#     H1 = [[len(H[i]), 0, H[i]] for i in range(len(H))]
#     for i in range(len(H)):
#         count = 0
#         for j in H[i]:
#             if "a" <= j <= "z":
#                 count += 1
#         H1[i][1] = count
#     H = H1
#
#     quicksort(0, len(H) - 1)
#     return H[-s][2]

def google(H, s):
    def compare(x, y):
        if x[0] > y[0]:
            return True
        if x[0] < y[0]:
            return False
        return x[1] >= y[1]

    def partition(p, r):
        x = H[r]
        i = p - 1
        for j in range(p, r):
            if compare(x, H[j]):
                i += 1
                H[i], H[j] = H[j], H[i]
        H[i+1], H[r] = H[r], H[i+1]
        return i + 1

    def select(p, k, r):
        if p == r:
            return H[p]
        if p < r:
            q = partition(p, r)
            if q == k:
                return H[q]
            elif q < k:
                return select(q+1, k, r)
            else:
                return select(p, k, q-1)

    H1 = [[len(H[i]), 0, H[i]] for i in range(len(H))]
    for i in range(len(H)):
        count = 0
        for j in H[i]:
            if "a" <= j <= "z":
                count += 1
        H1[i][1] = count
    H = H1
    result = select(0, len(H) - s, len(H) - 1)

    return result[2]


runtests(google, all_tests=True)
