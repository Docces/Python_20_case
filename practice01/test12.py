a = 0
b = 0
for i in range(1, 11):
    if i == 1:
        a += 100
    else:
        a += 100 / (2 ** (i - 2))
    if i == 10:
        b = 100 / (2 ** i)
print("第10次落地时经过了%f米，第十次弹起时的高度为%.10f米" % (a, b))

