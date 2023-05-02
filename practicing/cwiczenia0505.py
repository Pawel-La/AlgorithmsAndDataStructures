#Grafy
#
#
#1.Czy graf jest dwudzielny, dostajemy macierz M (dziala dla grafu spojnego)
#def zad(M):
#   size = len(M)
#   color = [0] * size
#   color[0] = 1
#   DFS(M,color,0)
#def DFS(M, n):
#   curr_color = color[n]
#   size = len(M)
#   for i in range(size):
#       if M[n][i] == 1:
#           if color[i] == curr_col:
#               return False
#           if color[i] == 0:
#               if curr_color == 1:
#                   color[i] = 2
#               else:
#                   color[i] = 1
#               if not DFS(M, i):
#                   return False
#   return True
#
#
#2.(zadanie jak na 3. kolosie moze byc) mamy spojny graf nieskierowany, chcemy pousuwac jego wierzcholki calkiem
#ale w takiej kolejnosci zeby w zadnym kroku graf nie byl niespojny
# ->odpalamy DFS normalnie
# ->jeśli przetwarzamy wierzchołek to możemy go usunąć
# ->czyli kolejność usuwania wierzchołów to będzie kolejność ich przetworzenia
#
# ->mozna tez BFS uzyc i usuwac wierzcholki o najwiekszych odległościach
#
#
#3. mamy graf nieskierowany zadany jako macierz, sprawdzic czy istnieje cykl o dokładnie 4 wierzchołkach
#   (O(n^3))
#   dla każdej pary (czyli n^2) sprawdzamy czy maja dwoch wspolnych sasiadow (n) bo wtedy znaczy ze jest cykl dlugosci 4
#
#
#4. mamy graf skierowany(zorientowany) i mamy cos takiego jak ujscie(wierzcholek do ktorego wchodza krawdzie i zadne nie wychodza)
#szukamy ujscia uniwersalnego czyli wszystkie wierzcholki musza wchodzic do danego wierzchołka. Dostajemy macierz sąsiedztwa
#0000
#1001
#1101
#1100
#jak jest 0 to idziemy w prawo, jak jest 1 to idziemy w doł, jak dojdziemy do prawego boku albo dolu to sprawdzamy dany indeks i(O(n))
#
#
#5. dana jest szachownica o wymiarach 8 x 8, w lewym gorny rogu jest krol, kazde pole ma swoj koszt (1 - 5) król chce trafic
#do prawego dolnego rogu, jaka jest najtansza droga. król może chodzic na dowolne sasiednie pole
#   ->BFS
#
#
#6. implementacja BFS ktory by wypisywał najkrótszą ścieżkę miedzy dwoma wierzchołkami s i t (proste, nudne, zakodowac)
#   ->robimy BFS
#   ->sprawdzajac parentów mozemy odtworzyc sciezke
#
#
#7.dany jest graf gdize kazda krawedz ma wage ze zbioru 1 - E, wagi krawedzi sa parami rozne
#algorytm ktory dla wierzcholkow x,y sprawdza czy istnieje sciezka po malejacych krawedziach
#   O(V+E)
#
#
#8.dana jest mapa krajow w postaci grafu i niektóre drogi są platne (1), a niektore darmowe (0)
#znalezc najtansza sciezke od A do B (modyfikacja DFS'a) i ją odtworzyć
#