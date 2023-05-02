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
    memo = [[(0,0) for _ in range(3)] for _ in range(count)]

    #i - numer punktu przesiadkowego z kolei ktory juz przejechalismy(numerowe od 0 do p-1 gdzie p to liczba punktów przesiadkowych
    #(traktujemy A jako punkt przesiadkowy na ktorym nie ma przesiadki))
    #j - przy ilu mijanych punktach kontrolnych kierowca byl Marian po dojechaniu do i+1 punktu przesiadkowego
    #val - {2,1,0} gdzie 2,1 oznaczaja ze aktualny kierowca moze jeszcze przejechac odpowednio 2,1 punktow przesiadkowych
    #0 oznacza ze musi byc przesiadka na nastepnym przystanku
    #who == True jesli kierowca jest Marian, who == False gdy kieruje Jacek
    #last_swap - indeks punktu przesiadkowego na ktorym byla ostatnia zmiana
    def f(i,j,val,who,last_swap):
        #przypadek koncowy tj rozwazylismy wszystkie punkty przesiadkowe, zwracamy liczbe przejechanych punktow kontrolnych przez Mariana i
        #do tego zwracamy tablice z indeksem ostatniej zmiany niestety nie zdazylem tego zrobic tak zeby zwracany indeks byl oryginalnym indeksem
        #w tym celu trzebaby skorzystac z tablicy T i orzyginalnej P
        if i == count:
            memo[val][i] = (j, [last_swap])
            return memo[val][i]
        #sytuacja gdy musi dojsc do zmiany na nastepnym postoju, dodajemy ostatni postoj do otrzymanego z rekurencji
        if val == 0:
            if who:
                a = f(i+1, j, 2, not who, i)
                a[1].append(last_swap)
                memo[val][i] = (a[0], a[1])
                return memo[val][i]
            else:
                a = f(i+1, j + T[i+1], 2, not who, i)
                a[1].append(last_swap)
                memo[val][i] = (a[0], a[1])
                return memo[val][i]
        #bierzemy mniejsza wartosc liczby przejechanych przez Mariana punktow kontrolnych i zwracamy tamta sciezke
        if who:
            a = f(i+1, j, 2, not who, i)
            b = f(i+1, j, val-1, who, last_swap)
            if a[0] < b[0]:
                a[1].append(last_swap)
                memo[val][i] = (a[0], a[1])
                return memo[val][i]
            else:
                b[1].append(last_swap)
                memo[val][i] = (b[0], b[1])
                return memo[val][i]
        else:
            a = f(i+1, j, val - 1, who, last_swap)
            b = f(i+1, j + T[i+1], 2, not who, i)
            if a[0] < b[0]:
                a[1].append(last_swap)
                memo[val][i] = (a[0], a[1])
                return memo[val][i]
            else:
                b[1].append(last_swap)
                memo[val][i] = (b[0], b[1])
                return memo[val][i]
    return f(0, 0, 2, False, -1)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )
