n = int(input())
num = 1
i = False

while num <= n:
    if num == n:
        i = True
        break
    if (n - num) % 3 == 0:
        num += 3
    elif (n - num) % 5 == 0:
        num += 5
    else:
        break
if i or num == n:
    print("YES")
else:
    print("NO")
