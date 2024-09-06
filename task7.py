def qavs(s):
    if len(s) == 1 or len(s) == 2:
        return s
    return s[0] + '(' + qavs(s[1:-1]) + ')' + s[-1]


print(qavs(input()))