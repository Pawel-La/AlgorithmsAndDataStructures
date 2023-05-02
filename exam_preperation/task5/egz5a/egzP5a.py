from egzP5atesty import runtests 


def inwestor(T):
    n = len(T)
    result = 0
    for i in T:
        max_count = 0
        count = 0
        for j in range(n):
            if T[j] >= i:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        max_count = max(max_count, count)
        result = max(result, max_count * i)
    return result


runtests(inwestor, all_tests=True)
