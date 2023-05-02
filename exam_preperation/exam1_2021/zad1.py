from zad1testy import runtests


def chaos_index(T):
    def merge_sort(T,a,b):
        def merge(x,y):
            i, j = 0, 0
            result = []
            while i < len(x) and j < len(y):
                if x[i] < y[j]:
                    result.append(x[i])
                    i += 1
                else:
                    result.append(y[j])
                    j += 1
            while i < len(x):
                result.append(x[i])
                i += 1
            while j < len(y):
                result.append(y[j])
                j += 1

            return result

        if a == b:
            return [T[a]]
        c = (a+b) // 2
        x = merge_sort(T, a, c)
        y = merge_sort(T, c+1, b)
        return merge(x,y)

    n = len(T)
    T = [(T[i], i) for i in range(n)]
    T = merge_sort(T, 0, n-1)
    result = 0
    for i in range(n):
        result = max(result, abs(i-T[i][1]))

    return result


#tab = [2,3,1,2,41,2]
#chaos_index(tab)
runtests(chaos_index)
