#Paweł Lamża
#Opis algorytmu:
#dla każdego otrzymanego słowa zapisujemy w tablicy tab na pozycji 0. jego dlugość, a na kolejnych pozycjach
#od 1. do 26. liczbę wystąpień w słowie konkretnych liter, gdzie 1. miejsce odpowiada 'a', 2. - 'b' itd.
#sortujemy tablice tab po kolejnych indeksach poczynając od liczby wystąpień 'z', a na dlugosci slowa kończąc
#używając do tego celu sortowania quicksort
#na koniec na posortowanej tablicy zliczamy popularność najpopularniejszego anagramu
#Złożoność czasowa: O(NlogN)
#Złożoność pamięciowa: O(N)

from kol1btesty import runtests


def counting_sort(t, n, k, index):
    tab1 = [0 for _ in range(n)]
    tab2 = [0 for _ in range(k+1)]

    for i in range(n):
        tab2[t[i][index]] += 1

    for i in range(1, k+1):
        tab2[i] += tab2[i-1]

    for i in range(n-1, -1, -1):
        tab1[tab2[t[i][index]] - 1] = i
        tab2[t[i][index]] -= 1

    tab3 = [[0 for _ in range(27)] for _ in range(n)]
    for i in range(n):
        for j in range(27):
            tab3[i][j] = t[tab1[i]][j]
    for i in range(n):
        for j in range(27):
            t[i][j] = tab3[i][j]


def f(T):
    n = len(T)
    #tablica [n][27] w której zliczamy liczbę liter kolejnych słów
    tab = [[0 for _ in range(27)] for _ in range(n)]
    #count - licznik na ktorym slowie jestesmy w danym momencie
    count = 0
    for i in T:
        word_len = 0
        #dla każdego słowa zwiększamy miejsce w tab odpowiadajace konkretnej literze i liczymy dlugosc slowa
        for j in i:
            tab[count][ord(j) - 96] += 1
            word_len += 1
        #zapisujemy dlugosc w 0. indeksie
        tab[count][0] = word_len
        count += 1
    #sortujemy tablice tab po kolejnych indeksach poczynając od liczby wystąpień 'z', a na dlugosci slowa kończąc
    for i in range(26, -1, -1):
        k = 0
        for j in range(n):
            k = max(k,tab[j][i])
        counting_sort(tab, count, k, i)

    #liczymy popularnosc najpopularniejszego anagramu
    i = 0
    max_popularity = 0
    while i < n:
        popularity = 0
        flag = True
        k = i
        while flag:
            popularity += 1
            k += 1
            for j in range(27):
                if k >= n or tab[i][j] != tab[k][j]:
                    max_popularity = max(max_popularity, popularity)
                    flag = False
                    break
        i = k
    return max_popularity


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
