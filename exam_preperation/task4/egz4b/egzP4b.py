from egzP4btesty import runtests 

class Node:
    def __init__(self, key, parent):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key
        self.x = None


def sol(root, T):
    def maximum(x):
        while x.right:
            x = x.right
        return x.key

    def minimum(x):
        while x.left:
            x = x.left
        return x.key

    def succ(x):
        if x.right:
            return minimum(x.right)
        else:
            while x.parent.key < x.key:
                x = x.parent
            if x.parent:
                return x.parent.key
            return None

    def pred(x):
        if x.left:
            return maximum(x.left)
        else:
            while x.parent.key > x.key:
                x = x.parent
            if x.parent:
                return x.parent.key
            return None

    result = 0
    for i in T:
        if 2*i.key == pred(i) + succ(i):
            result += i.key

    return result


runtests(sol, all_tests=True)
