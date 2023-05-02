from zad1ktesty import runtests

def roznica(s):
    print(s)
    n = len(s)
    global_min = 1
    tab_min = [0 for _ in range(n+1)]
    tab_min[0] = 0

    for i in range(1, n+1):
        if s[i-1] == '1':
            tab_min[i] = min(1, tab_min[i-1] + 1)
            global_min = min(global_min, tab_min[i])
        else:
            tab_min[i] = min(-1, tab_min[i-1] - 1)
            global_min = min(global_min, tab_min[i])
    sol = -global_min
    if global_min == 1:
        return -1
    return sol

runtests ( roznica )
