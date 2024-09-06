old = input()
old1 = old.replace('(', ')')


def stroka(s, new):
    if len(s) == 0:
        return new
    new = new + s[-1]
    return stroka(s[0:-1], new)


print(old + stroka(old1, new=''))