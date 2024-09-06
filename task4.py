def count_digits(s):
    kol = 0
    for char in s:
        if char.isdigit():
            kol += 1
    return kol

print(count_digits(input()))
