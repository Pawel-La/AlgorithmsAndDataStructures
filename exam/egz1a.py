#Paweł Lamża
#Złożoność O(n^3)
#w tablicy S_on_day_i liczymy ile sniegu bedzie na kazdym z obszarów po i dniach, przy czym zaczynamy w dniu 0.
#w tablicy T przechowujemy dane o tym ile sniegu mozna najwiecej w danym dniu zgromadzic bedac na danym obszarze,
#czyli kiedy wszystkie poprzednie obszary zostaly juz wyzerowane
#wykonujemy proste 3 pętle, jedna w drugiej dlatego otrzymujemy złożoność O(n^3)
#najlepszy wynik w kazdym dniu na danym obszarze to mozliwe najlepszy wynik w dniu kolejnym w nastepnym obszarze
#plus snieg na danym obszarze dzis
from egz1atesty import runtests

def snow(S):
    n = len(S)
    S_on_day_i = [[S[i] for i in range(n)] for _ in range(n)]

    for i in range(1, n):
        for j in range(n):
            S_on_day_i[i][j] = max(0, S_on_day_i[0][j] - i)

    T = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n-1, -1, -1):
        for j in range(n-1, i-1, -1):
            snow_ = 0
            for k in range(j+1, n+1):
                snow_ = max(snow_, T[i+1][k])
            T[i][j] = snow_ + S_on_day_i[i][j]

    #sprawdzamy i zwracamy największa liczbe sniegu z tablicy T
    result = 0
    for i in range(n):
        for j in range(n):
            result = max(result, T[i][j])

    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )

