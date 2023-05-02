#given number of stairs n, return how many diffrent ways to climb stairs are there
#if in each step we can go 2 stairs upwards or 1 step upwards


def stairs(n):
    tab = [-1 for _ in range(n+1)]
    tab[0] = 1
    tab[1] = 1
    for i in range(2, n+1):
        tab[i] = tab[i-1] + tab[i-2]
    return tab[n]

n = 6
print(stairs(n))
