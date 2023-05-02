def g(r):
    if r is None:
        return 0
    if r.left is None and r.right is None:
        return 0
    if r.right is None:
        return f(r.left)
    if r.left is None:
        return r.right.val
    return f(r.left) + f(r.right)


def f(r):
    if r is None:
        return 0
    if r.left is None and r.right is None:
        return r.val

    return max(g(r), g(r.left) + g(r.right) + r.val)


# result => f(root)

