def sitora(s, new):
    if len(s) == 0:
        return new[0:-1]
    new = new + s[0] + '*'
    return sitora(s[1:], new)


print(sitora(input(), new=''))