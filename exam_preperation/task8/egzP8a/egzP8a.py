from egzP8atesty import runtests 

# def reklamy ( T, S, o ):
#     def fine(a,b):
#         return a[1] < b[0] or b[1] < a[0]
#
#     n = len(T)
#     best = max(S)
#
#     for i in range(n):
#         for j in range(i+1, n):
#             if fine(T[i], T[j]):
#                 best = max(best, S[i] + S[j])
#     return best


def reklamy(T, S, o):
    best = max(S)
    n = len(T)

    T1 = [[S[i], T[i][1]] for i in range(n)]
    T1.sort(reverse=True)

    T2 = [[T[i][0], S[i]] for i in range(n)]
    T2.sort(reverse=True)

    i = 0
    j = 0
    while i < n and j < n:
        if T1[i][1] < T2[j][0]:
            best = max(best, T1[i][0] + T2[j][1])
        else:
            i += 1
        j += 1

    return best


runtests(reklamy, all_tests=True)
