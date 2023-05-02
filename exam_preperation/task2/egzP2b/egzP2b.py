from egzP2btesty import runtests
from math import log10


def kryptograf(D, Q):
    class BstNode:
        def __init__(self, key):
            self.key = key
            self.parent = None
            self.left = None
            self.right = None
            self.counter = 0

    root = BstNode('')
    for i in D:
        curr = root
        while len(i) >= 0:
            curr.counter += 1
            if len(i) == 0:
                break
            if i[-1] == '0':
                if curr.left is None:
                    curr.left = BstNode(i[-1] + curr.key)
                    curr.left.parent = curr
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BstNode(i[-1] + curr.key)
                    curr.right.parent = curr
                curr = curr.right
            i = i[:-1]

    result = 0
    for i in Q:
        curr = root
        while len(i) > 0:
            if i[-1] == '0':
                curr = curr.left
            else:
                curr = curr.right
            i = i[:-1]
        result += log10(curr.counter)

    return result


# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests=3)
