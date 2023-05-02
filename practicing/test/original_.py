#Paweł Lamża
#Opis algorytmu:
#dla każdego otrzymanego słowa zapisujemy w tablicy tab na pozycji 0. jego dlugość, a na kolejnych pozycjach
#od 1. do 26. liczbę wystąpień w słowie konkretnych liter, gdzie 1. miejsce odpowiada 'a', 2. - 'b' itd.
#sortujemy tablice tab po kolejnych indeksach poczynając od liczby wystąpień 'z', a na dlugosci slowa kończąc
#używając do tego celu sortowania quicksort
#na koniec na posortowanej tablicy zliczamy popularność najpopularniejszego anagramu
#Złożoność czasowa: O(NlogN)
#Złożoność pamięciowa: O(N)

# --------------------------> it might fing works?!!!!
import random

from kol1btesty import runtests


'''def quicksort(T, index, l, r):
    if l >= r:
        return
    i, j = l, r
    mid_val = T[(l+r) // 2][index]
    while i <= j:
        while T[i][index] < mid_val:
            i += 1
        while T[j][index] > mid_val:
            j -= 1
        if i <= j:
            #zamieniamy dwa wyrazy w tablicy tab
            for k in range(27):
                if T[i][k] != T[j][k]:
                    T[i][k], T[j][k] = T[j][k], T[i][k]
            i += 1
            j -= 1
    if l < j:
        quicksort(T, index, l, j)
    if i < r:
        quicksort(T, index, i, r)'''


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
        quicksort(tab, i, 0, n - 1)


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
#runtests( f, all_tests=True )

tab = [[random.randint(1,3) for _ in range(2)] for _ in range(10)]
for k in tab:
    for j in k:
        print(j, end=" ")
    print()
print()

for i in range(1, -1, -1):
    quicksort(tab,i,0,len(tab)-1, 2)
    for k in tab:
        for j in k:
            print(j, end=" ")
        print()
    print()

