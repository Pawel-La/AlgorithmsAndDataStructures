#Paweł Lamża
#Opis algorytmu: wykonuje sortowanie quicksort rosnąco po początkach przedziałów, przy czym jeśli dwa
#przedziały mają ten sam początek to wcześniej będzie ten z nich, który ma dalszy koniec.
#Następnie iteruje po posortowanej tablicy zliczając ile przedziałów zawiera w sobie dany przedział A
#(zauważmy, że po moim posortowaniu wszystkie przedziały zawierające się w A mają większy indeks w tablicy niż ma A)
#,z tym że jeśli zawiera jakiś przedział B to zaznaczam iż przedział B nie jest przedziałem zawierającym najwięcej
#innych przedziałów i dla przedziału B nie zliczam liczby przedziałów jakie zawiera w sobie
#
#Złożoność obliczeniowa: O(n^2)

from zad2testy import runtests


def quicksort(t, left, right):
    if left >= right:
        return
    i = left
    j = right
    pivot = t[(left+right) // 2]
    p0 = pivot[0]
    p1 = pivot[1]
    while True:
        while p0 > t[i][0] or (p0 == t[i][0] and p1 < t[i][1]):
            i += 1
        while p0 < t[j][0] or (p0 == t[j][0] and p1 > t[j][1]):
            j -= 1
        if i < j:
            t[i], t[j] = t[j], t[i]
            i += 1
            j -= 1
        elif i == j:
            i += 1
            j -= 1
        else:
            break
    if j > left:
        quicksort(t, left, j)
    if i < right:
        quicksort(t, i, right)


def depth(L):
    n = len(L)
    quicksort(L, 0, n-1)
    tab = [True for _ in range(n)]
    max_count = 0
    for i in range(n):
        if tab[i]:
            if max_count > n - i:
                break
            start_of_i = L[i][0]
            end_of_i = L[i][1]
            count = 0
            for j in range(i+1, n):
                start_of_j = L[j][0]
                end_of_j = L[j][1]
                if start_of_i <= start_of_j and end_of_j <= end_of_i:
                    count += 1
                    tab[j] = False
                elif end_of_i <= start_of_j or not count:
                    break
            max_count = max(max_count, count)

    return max_count


runtests( depth )
