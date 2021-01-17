a = int(input("请输入一个整数："))
b = []
print("%d=" % a, end='')
while True:
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            b.append(str(i))
            a = int(a / i)
            break
    else:
        b.append(str(a))
        break
print("*".join(b))
