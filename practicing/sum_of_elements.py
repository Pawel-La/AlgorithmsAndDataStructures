# given an array t with n natural numbers init and value x
# is there a sum of some chosen elements from t equal to x?
# return True/False
# for example if u got array [1,4,2,52,3] and x == 7, program should return True, cuz 4+3 == 7

import random


def sum_of_el(t, x, i, memo={}):
    if (x, i) in memo:
        return memo[(x, i)]
    if i <= 0:
        return False
    if x < 0:
        memo[(x, i)] = False
        return False
    if x == 0:
        memo[(x,i)] = True
        return True


    result = sum_of_el(t, x, i-1, memo) or sum_of_el(t, x - t[i-1], i-1, memo)
    memo[(x,i)] = result
    return result


#can also be done nonrecursive way as below with a use of 2d array:
'''def func(t, x):
   n = len(t)
   f = [[0 for _ in range(x)] for _ in range(n)]
   for i in range(n):
       f[i][0] = 1
   for i in range(1,n):
       for j in range(1,x):
           if j - A[i] >= 0:
               f[i][j] = f[i-1][j-A[i]] or f[i-1][j]
           else:
               f[i][j] = f[i-1][j]
   return f[n-1][x-1]'''
