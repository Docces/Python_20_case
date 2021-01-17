num = 0
a = [0, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    a[2] += 1
for i in range(month):
    num += a[i]
num += day
print("%d年%d月%d号是今年第%d天" % (year, month, day, num))
