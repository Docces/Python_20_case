# i为第一个完全平方数
n = 0
while (n + 1) ** 2 - n * n <= 168:
    n += 1

for i in range((n + 1) ** 2):
    for j in range(n + 1):
        if j ** 2 == i:
            for k in range(n + 1):
                if k ** 2 == i + 168:
                    print(i - 100)
# 或者可以使用下面这种方法
for i in range((n + 1) ** 2):
    if i ** 0.5 == int(i ** 0.5) and (i + 168) ** 0.5 == int((i + 168) ** 0.5):
        print(i - 100)
