def robber(t):
    n = len(t)
    val = [0] * n
    val[n-1] = t[n-1]
    val[n-2] = max(t[n-2], t[n-1])

    for i in range(n - 3, -1, -1):
        val[i] = max(val[i+1], t[i] + val[i+2])

    return val[0]

def robber2(t):
    t1 = t[1:]
    t2 = t[:-1]
    return max(robber(t1), robber(t2))
