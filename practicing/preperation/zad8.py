from zad8ktesty import runtests
def solution(s,t):
    l1 = len(s)
    l2 = len(t)
    tab = [[-1 for _ in range(l2+1)] for _ in range(l1+1)]

    def napraw(i=0, j=0):
        if tab[i][j] != -1:
            return tab[i][j]
        while i < l1 and j < l2 and s[i] == t[j]:
            i += 1
            j += 1

        if i >= l1:
            tab[i][j] = l2 - j
            return tab[i][j]
        if j >= l2:
            tab[i][j] = l1 - i
            return tab[i][j]

        tab[i][j] = 1 + min(napraw(i+1, j), napraw(i, j+1), napraw(i+1, j+1))

        return tab[i][j]

    return napraw()


runtests(solution)
