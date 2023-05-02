from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None

def wybory(T):
    result = 0
    for i in T:
        money = i.fundusze
        n = 0
        T1 = []
        while i is not None:
            T1.append((i.wyborcy, i.koszt))
            i = i.next
            n += 1
        tab = [[0 for _ in range(money + 1)] for _ in range(n + 1)]
        for j in range(1, n + 1):
            for k in range(1, money + 1):
                tab[j][k] = max(tab[j-1][k], tab[j][k-1])
                if k >= T1[j-1][1]:
                    tab[j][k] = max(tab[j][k], tab[j-1][k-T1[j-1][1]] + T1[j-1][0])
        result += tab[n][money]
    return result


runtests(wybory, all_tests=True)
