from zad3testy import runtests


def lamps(n, operations):
    t = [0 for _ in range(n)]
    count = 0
    result = 0
    for a, b in operations:
        for i in range(a, b+1):
            t[i] += 1
            t[i] %= 3
            if t[i] == 2:
                count += 1
            elif t[i] == 0:
                count -= 1

        result = max(result, count)

    return result

    
runtests(lamps)
