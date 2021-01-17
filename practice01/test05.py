raw = []
for i in range(1, 4):
    a = int(input("请输入第%d个数:" % i))
    raw.append(a)

j = 0
k = 0
while True:
    for m in range(len(raw)):
        if j == raw[m]:
            print(j, end=' ')
            k += 1
    j += 1
    if k == len(raw):
        break

for i in range(len(raw)):
    for j in range(i, len(raw)):
        if raw[i] > raw[j]:
            raw[i], raw[j] = raw[j], raw[i]
print(raw)
