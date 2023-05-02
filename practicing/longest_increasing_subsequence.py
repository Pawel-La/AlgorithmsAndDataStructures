#return length of longest increasing subsequance, not neccesary continously,
#for example in [1,4,9,3,5,6] its [1,3,5,6] so it should return 4

def longest_subsequence(t):
    n = len(t)
    LIN = [1] * n
    for i in range(n -1, -1, -1):
        for j in range(i + 1, n):
            if t[i] < t[j]:
                LIN[i] = max(LIN[i], 1+LIN[j])
    return max(LIN)

tab = [1,3,2,4,1,5,1,13,42,4]
print(longest_subsequence(tab))
