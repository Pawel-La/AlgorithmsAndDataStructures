# given an array with numbers and target sum, add or substract each of nums
# and return how many of sums are equal to given target
def target_sums_num(t, target):
    memo = {}

    def backtrack(i, total):
        if (i, total) in memo:
            return memo[(i, total)]
        if i == len(t):
            return 1 if total == target else 0
        memo[(i, total)] = (backtrack(i + 1, total + t[i]) +
                            backtrack(i + 1, total - t[i]))
        return memo[(i, total)]

    return backtrack(0, 0)
