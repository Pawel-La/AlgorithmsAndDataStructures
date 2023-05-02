# given 2d array MxN of costs, what is the cheapest way from top left corner
# to bottom right corner. return road we chose we can only move right or down, R for right, D for down
# for example given an array:
#   1 4 3
#   4 6 2
#   2 1 1
# program should return DDRR cuz 1+4+2+1+1 = 9 is the lowest cost to get from start to end

# version that returns lowest cost
def cheapest_road(t, x=0, y=0, memo={}):
    val = t[x][y]
    n = len(t)
    m = len(t[0])

    if (x, y) in memo:
        return memo[x, y]
    if x == n - 1 and y == m - 1:
        memo[x, y] = val
        return val
    if x == n - 1:
        memo[x, y] = cheapest_road(t, x, y+1, memo) + val
        return memo[x, y]
    if y == m - 1:
        memo[x, y] = cheapest_road(t, x+1, y, memo) + val
        return memo[x, y]

    memo[x, y] = min(cheapest_road(t, x+1, y), cheapest_road(t, x, y+1)) + val
    return memo[x, y]


# version nonrecursive
def cheapeast_road2(t):
    n = len(t)
    m = len(t[0])
    t2 = [[t[j][i] for i in range(m)] for j in range(n)]

    for i in range(m - 2, -1, -1):
        t2[n-1][i] += t2[n-1][i+1]
    for i in range(n - 2, -1, -1):
        t2[i][m-1] += t2[i+1][m-1]

    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            t2[i][j] += min(t2[i+1][j], t2[i][j+1])

    return t2[0][0]


# now right solution with returning string with direction of moves
# we gonna simply change a bit our nonrecursive solution
def solution(t):
    result = ""
    n = len(t)
    m = len(t[0])
    t2 = [[t[j][i] for i in range(m)] for j in range(n)]

    for i in range(m - 2, -1, -1):
        t2[n-1][i] += t2[n-1][i+1]
    for i in range(n - 2, -1, -1):
        t2[i][m-1] += t2[i+1][m-1]

    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            t2[i][j] += min(t2[i+1][j], t2[i][j+1])

    i, j = 0, 0
    while (i,j) != (n-1,m-1):
        if i == n - 1:
            result += "R"
            j += 1
        elif j == m - 1 or t2[i+1][j] < t2[i][j+1]:
            result += "D"
            i += 1
        else:
            result += "R"
            j += 1

    return result
