from egzP4atesty import runtests 


# def mosty(T):
#     T.sort()
#     tab = [T[i][1] for i in range(len(T))]
#     best = [1 for _ in range(len(tab))]
#     for i in range(1, len(tab)):
#         for j in range(i):
#             if tab[j] <= tab[i]:
#                 best[i] = max(best[i], best[j] + 1)
#     return max(best)

def mosty(T):
    def find(x, a, b):
        if a > b:
            return a
        c = (a + b) // 2
        if x >= sol[c]:
            return find(x, c+1, b)
        elif x < sol[c]:
            return find(x, a, c-1)

    T.sort()
    T = [T[i][1] for i in range(len(T))]
    sol = [T[0]]
    for i in range(1, len(T)):
        f = find(T[i], 0, len(sol) - 1)
        if f == len(sol):
            sol.append(T[i])
        else:
            sol[f] = T[i]

    return len(sol)


runtests(mosty, all_tests=True)
