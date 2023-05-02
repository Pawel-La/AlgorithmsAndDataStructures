#Paweł Lamża
#puszczamy BFS-a ktory w kazdym wierzcholku wpisze odleglosc od roota
#usuwamy po kolei kazda permutacje mozliwa i dla niej sprawdzamy ile dane drzewo ma szerokosci i wysokosci
#na koniec zwracamy minimalna liczbe krawedzi do usuniecia
#bruteforce O(n^n)


from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

def wideentall( T ):
    width = 0
    length = 0
    def func(T, count):
        T1 = T
        T1.left = None
        T2 = T
        T2.right = None
        return min(func(T1.right, count+1), func(T2.left, count+1),  func(T.right, count), func(T.left, count))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )