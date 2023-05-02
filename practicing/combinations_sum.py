def comb(candidates, target):
    result = []

    def comb_sum(c, t, last=0, tab=[]):
        if t == 0:
            result.append(tab)
            return

        n = len(c)
        for j in range(last, n):
            if t - c[j] >= 0:
                tab1 = tab.copy()
                tab1.append(c[j])
                comb_sum(c, t - c[j], j, tab1)

    comb_sum(candidates, target)
    return result
