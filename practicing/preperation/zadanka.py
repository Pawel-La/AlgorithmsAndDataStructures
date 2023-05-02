#staircase
import collections


def staircase(n):
    T = [0 for _ in range(n+1)]
    T[0] = 1
    T[1] = 1
    for i in range(2, n+1):
        T[i] = T[i-1] + T[i-2]
    return T[n]

#cost staircase
def staircase_with_cost(T):
    n = len(T)
    tab = [0 for _ in range(n)]
    tab[0] = T[0]
    tab[1] = T[1]
    for i in range(2, n):
        tab[i] = T[i] + min(tab[i-1], tab[i-2])

    return min(tab[n-2], tab[n-1])

#house robber 1
def house_robber(T):
    n = len(T)
    tab = [0 for _ in range(n)]
    tab[0] = T[0]
    tab[1] = max(T[0], T[1])

    for i in range(2, n):
        tab[i] = max(tab[i-1], tab[i-2] + T[i])

    return tab[n-1]

#house robber 2
def house_robber2(T):
    n = len(T)
    tab = [0 for _ in range(n)]
    tab[0] = T[0]
    tab[1] = max(T[0], T[1])

    for i in range(2, n-1):
        tab[i] = max(tab[i-1], tab[i-2] + T[i])
    sol = tab[n-2]

    tab[1] = T[1]
    tab[2] = max(T[1], T[2])
    for i in range(3, n):
        tab[i] = max(tab[i-1], tab[i-2] + T[i])
    sol = max(sol, tab[n-1])

    return sol

#house robber 3
def house_robber_3(T):
    n = len(T)
    f_tab = [-1 for _ in range(n)]
    g_tab = [-1 for _ in range(n)]

    def left(i):
        return 2*i + 1
    def right(i):
        return 2*i + 2
    def parent(i):
        return (i - 1) // 2

    #func f returns biggest possible value we can get to i-th place
    def f(i):
        if f_tab[i] != -1:
            return f_tab[i]
        if T[i] is None:
            return 0
        if left(i) >= n:
            f_tab[i] = T[i]
            return f_tab[i]

        f_tab[i] = max(T[i] + g(left(i)) + g(right(i)), g(i))
        return f_tab[i]

    #func g returns biggest possible value we can get to i-th place but we don't rob i-th house
    def g(i):
        if g_tab[i] != -1:
            return g_tab[i]
        if left(i) >= n:
            g_tab[i] = 0
            return 0
        g_tab[i] = f(left(i)) + f(right(i))
        return g_tab[i]

    return f(0)

#longest palindromic substring
def longest_palindromic_substring(s):
    n = len(s)
    max_string = ""

    for i in range(n):
        x, y = i-1, i+1
        while x >= 0 and y < n and s[x] == s[y]:
            x -= 1
            y += 1
        if y - x - 1 > len(max_string):
            max_string = s[x+1:y]

    for i in range(n):
        x, y = i, i+1
        while x >= 0 and y < n and s[x] == s[y]:
            x -= 1
            y += 1
        if y - x - 1 > len(max_string):
            max_string = s[x+1:y]

    return max_string


#palindromic substring
def palindromic_substring(s):
    n = len(s)
    count = 0
    for i in range(n):
        x1, y1 = i, i
        x2, y2 = i, i+1
        while x1 >= 0 and y1 < n and s[x1] == s[y1]:
            count += 1
            x1 -= 1
            y1 += 1
        while x2 >= 0 and y2 < n and s[x2] == s[y2]:
            count += 1
            x2 -= 1
            y2 += 1
    return count


#zwracanie najkrotszej sciezki w grafie:
from collections import deque
def solution(M,s,t):
    n = len(M)
    q = collections.deque()
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    d = [-1 for _ in range(n)]
    q.append(s)
    d[s] = 0
    visited[s] = True

    while not visited[t] and q:
        val = q.popleft()
        for i in range(n):
            if M[val][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)
                d[i] = d[val] + 1
                parent[i] = val

    if visited[t]:
        l = d[t] + 1
        sol = [0 for _ in range(l)]
        x = t
        for i in range(l-1, -1, -1):
            sol[i] = x
            x = parent[x]
    else:
        return None

    return sol


#racksack
def rucksack(weight, value, capacity):
    n = len(weight)
    tab = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            tab[i][j] = tab[i-1][j]
            if j >= weight[i-1]:
                tab[i][j] = max(tab[i][j], tab[i-1][j-weight[i-1]] + value[i-1])
    res = []
    i = n
    j = capacity
    while i > 0:
        if tab[i-1][j] != tab[i][j]:
            res.append(i-1)
            j -= weight[i-1]
        i -= 1
    return sorted(res)





w = [1,1,1,2,2]
v = [3,4,4,3,8]
cap = 6
print(rucksack(w,v,cap))
