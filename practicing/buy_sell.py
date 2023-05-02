#given array of prices on each day return what is the biggest profit u can make
#by buying on day A and selling on day B, A < B

def buy_sell(t):
    n = len(t)
    b = 0
    s = 1
    profit = 0
    while s < n:
        if t[b] >= t[s]:
            b = s
        else:
            profit = max(profit, t[s] - t[b])
        s += 1
    return profit

tab = [7,5,1,3,5,4,6,1,3]
print(buy_sell(tab))
