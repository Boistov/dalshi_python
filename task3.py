def stroka(s, kol):
    if len(s) == 0:
        return kol
    elif s[0].isdigit():
        kol += 1
    return stroka(s[1::], kol)

print(stroka(input(), kol=0))