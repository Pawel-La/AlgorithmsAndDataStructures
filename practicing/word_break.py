#given a string s and a dictionary of words word_dict, return True if s can be
#broken into words that each word belongs to word_dict
#for example s = "portugal", word_dict = ["po", "ga", "rtu", "l"]
#program should return True cause "portugal" = "po" + "rtu" + "ga" + "l"


def word_break(s, d, memo={}):
    len_s = len(s)
    if not len_s:
        return True
    if s in memo:
        return memo[s]

    for word in d:
        x = len(word)
        if x <= len_s and word == s[:x]:
            if word_break(s[x:], d, memo):
                memo[s[x:]] = True
                return True

    memo[s] = False
    return False
