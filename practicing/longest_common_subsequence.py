# given two arrays with numbers, we seeking length of the longest common subsequence
# for example given [1,4,3,1,23,4,5] and [4,3,2,1,5,3]
# program should return 4 cuz [4,3,1,5] is longest common subs of these two arrays


def longest_common_subsequence(t1, t2):
    m = len(t1)
    n = len(t2)
    t = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if t1[i] == t2[j]:
                t[i][j] = 1 + t[i+1][j+1]
            else:
                t[i][j] = max(t[i+1][j], t[i][j+1])

    return t[0][0]
