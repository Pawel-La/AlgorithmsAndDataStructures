from zad7testy import runtests

def droga( G ):
    n = len(G)
#   parents - array of parents
    parents = [-1 for _ in range(n)]
#   function recursive going through graph and checking possible ways, if found one than return it
#   num - number of cities already visited, p -(parent)index of the latest city visited before actual, i - index city
    def dfs(num, p, i):
#       we check if we are at city 0.
        if not i:
#           if we are here and we visited all cities already than checking which gate we entered it (it must be south)
            if num == n:
                if p in G[0][1]:
                    return p
                return 0
#           if we are here for the first time we don't want to return 0
            if p != -1:
                return 0
#       if we entering other city than 0 for the second time return 0
        if parents[i] != -1:
            return 0
#       setting parent of i to parent given to our function
        parents[i] = p
#       checking which gate we have to leave the city 0 - north, 1 - south
        direction = 0
        if p in G[i][0]:
            direction = 1
#       checking all possible ways of going through graph
        for el in G[i][direction]:
            x = dfs(num+1, i, el)
            if x:
                return x
#       if we haven't found a way here we delete latest move (backtracking)
        parents[i] = -1
        return 0

#   starting from city 0 and we leave by north gate from here
    x = dfs(0, -1, 0)
    if x:
        sol = [-1 for _ in range(n)]
        for i in range(n-1, -1, -1):
            sol[i] = x
            x = parents[x]
        return sol

    return None

#   zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )
