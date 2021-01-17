mouth = int(input("请输入繁殖月份："))
a = 1
b = []
for i in range(mouth):
    if i - 2 <= 0:
        b.append(a)
    else:
        a += b[i - 2]
        b.append(a)
m = 1
for n in b:
    print("第%d个月的兔子总数是：%d" % (m, n))
    m += 1

