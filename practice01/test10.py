a = input("请输入一个值：")
b = int(input("请输入相加次数："))
c = [int(a*i) for i in range(1, b + 1)]
d = [str(j) for j in c]
print("s=%d=" % sum(c) + '+'.join(d))
