a = []
m = 0
for i in range(2, 1000):
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            m += j
            if i / j != i:
                m += i / j
    if m == i:
        a.append(int(m))
    m = 0
print(a)
