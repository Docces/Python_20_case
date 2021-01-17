h = int(input("请输入菱形高度："))
a = h
b = h
for i in range(1, h+1):  # 正三角
    print(" "*(a-1), "*"*(2*i - 1))
    a -= 1
for j in range(1, h):  # 倒三角
    print(" "*j, "*"*(2*b-3))
    b -= 1

