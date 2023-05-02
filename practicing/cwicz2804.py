#           ALGORYTMY ZACHLANNE
#   1.Mamy dany zbior zadan T: T1 -> Tn i kazde zadanie posiada termin jednostkowy d(Ti) i zysk za wykonanie w terminie g(Ti)
#   Jesli zadanie zostanie wykonane w czasie przed terminem otrzymujemy zysk. Wykonanie zadania trwa jednostke czasu
#   Szukamy maksymalny zysk
#
#   2.ładowanie przyczepy, mamy przyczepe o pojemnosci K kilogramow i zbior ladunkow o wagach danych w1,..,wn
#   waga kazdego z ladunkow jest potega dwojki np. 2,2,4,8,1,8,16 K = 27
#   Podac algo zachlanny ze przyczepa jest maksymalnie zapelniona i zeby bylo jak najmniej ladunkow
#   ->bierzemy najciezszy LOL
#
#   3.tablica A chcemy znalezc taka liczbe ze wartosc sumy odleglosci danej liczby od pozostałych jest minimalna
#   ->bierzemy wartosc srodkowa (n//2)
#
#   4.czołg jedzie z punktu A do B i spala paliwo jedno na jedna jednostke. na stacjach tankuje do pełna, gdzie tankowac,
#   zeby zatrzymac sie najmniej razy. L - pojemność baku (v1. na kazdej stacji inny koszt paliwa, v1. = v2. + na kazdej stacji do pelna)
#   ->na ostatniej możliwej tankujemy do maksa

def sort_(el):
    return el[1]


def zad1(T):
    n = len(T)
    T = sorted(T, key=sort_)
    time = T[n-1][1]
    T = sorted(T, reverse=True)

    tab = [0 for _ in range(time+1)]
    res = 0
    for i in T:
        v, t = i[0], i[1]
        while t >= 0 and tab[t] != 0:
            t -= 1
        if t >= 0:
            res += v
            tab[t] = v

    return res


