def salom(num):
    if len(num) == 1 or len(num) == 0:
        return num
    elif len(num) == 2 and num[0] != num[-1]:
        return num
    elif num[0] == num[-1]:
        num = num[1:-1]
        return salom(num)
    return num[0] + salom(num[1:-1]) + num[-1]


print(salom(input()))