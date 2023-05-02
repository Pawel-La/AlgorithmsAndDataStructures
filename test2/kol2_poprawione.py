#Paweł Lamżą
#w tablicy 3 na count gdzie count to liczba punktow przesiadkowych minus jeden zapisujemy wybrane punkty wraz z tym jak duzo
#punktow kontrolnych przejechal Marian
#opis szerszy nizej
#
#zlozonosc O(n) niestety chyba nie zdaze dokonczyc pisac programu

from kol2atesty import runtests
def drivers( P, B ):
    #tablica T - przechowuje dane o tym ile punktow kontrolnych musi przejechac kierowca miedzy i-tym a i+1-ym punktem przesiadkowym
    P1 = sorted(P)
    n = len(P)
    count = 0
    T = [0 for _ in range(n-1)]
    x = 0
    #szukamy pierwszego punktu postojowego
    while P1[x][1] != True:
        x += 1
    for el in range(x+1, n):
        if P1[el][1]:
            count += 1
        else:
            T[count] += 1
    count += 1
    #w zmiennej count przechowujemy teraz zatem ile jest stacji przesiadkowych
    #zapamietujemy dla zmiennej val(ktora moze miec wartosci od 0 do 2, wiecej o niej ponizej) oraz liczby count
    #pierwszym argumentem jest to kto jest teraz za kierownica

    memo = [[[-1 for _ in range(count+1)] for _ in range(3)] for _ in range(2)]

    #i - numer punktu przesiadkowego z kolei ktory juz przejechalismy(numerowe od 0 do p-1 gdzie p to liczba punktów przesiadkowych
    #(traktujemy A jako punkt przesiadkowy na ktorym nie ma przesiadki))
    #j - przy ilu mijanych punktach kontrolnych kierowca byl Marian po dojechaniu do i+1 punktu przesiadkowego
    #val - {2,1,0} gdzie 2,1 oznaczaja ze aktualny kierowca moze jeszcze przejechac odpowednio 2,1 punktow przesiadkowych
    #0 oznacza ze musi byc przesiadka na nastepnym przystanku
    #who == True jesli kierowca jest Marian, who == False gdy kieruje Jacek
    #last_swap - indeks punktu przesiadkowego na ktorym byla ostatnia zmiana
    def f(i, val, who):
        #przypadek koncowy tj rozwazylismy wszystkie punkty przesiadkowe, zwracamy liczbe przejechanych punktow kontrolnych przez Mariana i
        #do tego zwracamy tablice z indeksem ostatniej zmiany niestety nie zdazylem tego zrobic tak zeby zwracany indeks byl oryginalnym indeksem
        #w tym celu trzebaby skorzystac z tablicy T i oryginalnej P
        if memo[who][val][i] != -1:
            return memo[who][val][i]
        if i == count:
            memo[who][val][i] = 0
            return memo[who][val][i]
        #sytuacja gdy musi dojsc do zmiany na nastepnym postoju, dodajemy ostatni postoj do otrzymanego z rekurencji
        if val == 0:
            if who:
                memo[who][val][i] = f(i+1, 2, (who + 1) % 2)
                return memo[who][val][i]
            else:
                memo[who][val][i] = f(i+1, 2, (who + 1) % 2) + T[i]
                return memo[who][val][i]
        #bierzemy mniejsza wartosc liczby przejechanych przez Mariana punktow kontrolnych i zwracamy tamta sciezke
        else:
            if who:
                a = f(i+1, 2, (who + 1) % 2)
                b = f(i+1, val-1, who) + T[i]
                if a < b:
                    memo[who][val][i] = a
                    return memo[who][val][i]
                else:
                    memo[who][val][i] = b
                    return memo[who][val][i]
            else:
                a = f(i+1, val - 1, who)
                b = f(i+1, 2, (who + 1) % 2) + T[i]
                if a < b:
                    memo[who][val][i] = a
                    return memo[who][val][i]
                else:
                    memo[who][val][i] = b
                    return memo[who][val][i]
    x = f(0, 2, 0)
    return x

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( drivers, all_tests = False )
