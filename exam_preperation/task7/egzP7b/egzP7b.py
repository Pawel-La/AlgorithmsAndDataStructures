from egzP7btesty import runtests


def ogrod(S, V):
    n = len(S)
    m = len(V)
    tab = [[0 for _ in range(m)] for _ in range(n)]

    result = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            if tab[i][S[j] - 1] == 0:
                sum += V[S[j] - 1]
                if sum > result:
                    result = max(result, sum)
            elif tab[i][S[j] - 1] == 1:
                sum -= V[S[j] - 1]
            tab[i][S[j] - 1] += 1

    return result


runtests(ogrod, all_tests=True)
