a = 0
b = []
for i in range(100, 201):
    for j in range(2, int(i**0.5)):
        if i % j == 0:
            break
    else:
        b.append(i)
        a += 1
print("一共有%d个质数" % a)
print(b)
