from egzP1atesty import runtests 


def change_word_to_morse(word, M):
    result = ''
    for i in word:
        result += M[ord(i)-65][1]
    return result


def titanic(W, M, D):
    #saving what signs we can use in tab
    W = change_word_to_morse(W, M)
    tab = [False for _ in range(32)]
    for i in D:
        sign = M[i][1]
        count = 0
        for j in range(len(sign)):
            count *= 2
            count += 1
            if sign[j] == '-':
                count += 1
        tab[count] = True
    #now the solution itself
    how_many_signs = [float('inf') for _ in range(len(W) + 1)]
    how_many_signs[0] = 0

    for i in range(1, len(W) + 1):
        val = how_many_signs[i-1]
        count = 0
        signs = 0
        while count < 32:
            if i+signs >= len(W) + 1:
                break
            count *= 2
            count += 1
            if W[i-1+signs] == '-':
                count += 1
            if count < 32 and tab[count]:
                how_many_signs[i + signs] = min(how_many_signs[i + signs], val + 1)
            signs += 1

    return how_many_signs[-1]


runtests(titanic, recursion=False)
