def dig_pow(n, p):
    a = [int(i) for i in str(n)]
    s = 0
    for j in range(len(a)):
        s += a[j] ** (p + j)
    return s // n if s % n == 0 else -1


print(dig_pow(89, 1))
