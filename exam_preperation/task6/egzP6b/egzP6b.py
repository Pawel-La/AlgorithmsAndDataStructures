from egzP6btesty import runtests 


def jump(M):
    def transform(x):
        result = [0,0]

        if x[0] == 'U':
            result[0] = 2
        elif x[0] == 'D':
            result[0] = -2
        elif x[0] == 'L':
            result[1] = -2
        elif x[0] == 'R':
            result[1] = 2

        if x[1] == 'U':
            result[0] = 1
        elif x[1] == 'D':
            result[0] = -1
        elif x[1] == 'L':
            result[1] = -1
        elif x[1] == 'R':
            result[1] = 1

        return result

    dictionary = {}
    count = 1
    position = (0, 0)
    dictionary[position] = 1

    for i in M:
        #d - directions
        d = transform(i)
        position = (position[0] + d[0], position[1] + d[1])
        if dictionary.get(position):
            dictionary[position] += 1
            if dictionary[position] % 2 == 0:
                count -= 1
            else:
                count += 1
        else:
            dictionary[position] = 1
            count += 1
    return count


runtests(jump, all_tests=True)
