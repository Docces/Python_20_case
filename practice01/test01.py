total = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                a = i * 100 + j * 10 + k
                print(a)
                total += 1
print(total)

b = [i * 100 + j * 10 + k for i in range(1, 5)
     for j in range(1, 5) for k in range(1, 5)
     if (i != j) and (i != k) and (j != k)]
print(len(b))
print(b)

# 回溯算法
a = [1, 2, 3, 4]
res = []
used = [False] * len(a)


def dfs(lst, temp, num):
    if len(temp) == num:
        res.append(temp)
        return
    for x in range(len(lst)):
        if not used[x]:
            used[x] = True
            temp += str(lst[x])
            dfs(lst, temp, num)
            temp = temp[:-1]
            used[x] = False
    return


dfs(a, "", 3)
res = [int(i) for i in res]
print(res)
print(len(res))
