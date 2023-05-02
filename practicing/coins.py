# give an array with nominals of coins and a value we want to get
# program should return minimal number of coins that is needed to get our value

def coins(t, x):
    tab = [-1 for _ in range(x + 1)]
    tab[0] = 0

    for i in range(x):
        if tab[i] != -1:
            for j in t:
                if i + j <= x:
                    if tab[i + j] == -1:
                        tab[i + j] = tab[i] + 1
                    else:
                        tab[i + j] = min(tab[i] + 1, tab[i + j])

    return tab[x]

