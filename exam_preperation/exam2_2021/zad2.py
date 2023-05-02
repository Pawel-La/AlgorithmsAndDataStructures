from zad2testy import runtests


def balance(T):
    def setting_values(T):
        n = len(T.edges)
        for i in range(n):
            if T.edges[i] != T.parent:
                T.edges[i].parent = T
                T.value += T.weights[i]
                T.value += setting_values(T.edges[i])
        return T.value

    def searching_result(T, sum):
        nonlocal best
        nonlocal best_id
        n = len(T.edges)
        for i in range(n):
            if T.edges[i] != T.parent:
                if best > abs(T.edges[i].value - (sum - T.weights[i])):
                    best = abs(T.edges[i].value - (sum - T.weights[i]))
                    best_id = T.ids[i]
                searching_result(T.edges[i], sum)

    best = float("inf")
    best_id = -1
    setting_values(T)
    sum = T.value
    searching_result(T, sum)
    return best_id

    
runtests( balance )


