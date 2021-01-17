# Python_20_case
20道Python基础练习题
#### 练习01 数字组合
> 有四个数字：1、2、3、4，其能组成多少个互不相同且无重复数字的三位数？各是多少？
```python
total = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                print(i, j, k)
                total += 1
print(total)

b = [i * 100 + j * 10 + k for i in range(1, 5) for j in range(1, 5) for k in range(1, 5) if (i != j) and (i != k) and (j != k)]
print(len(b))
print(b)
```
另外可以采用**回溯算法**

```python
# 回溯算法
a = [1, 2, 3, 4]
res = []
used = [False] * len(a) #剔除重复数

def dfs(lst, temp, num):
    if len(temp) == num:
        res.append(temp)
        return
    for i in range(len(lst)):
        if not used[i]:
            used[i] = True
            temp += str(lst[i])
            dfs(lst, temp, num)
            temp = temp[:-1] #回溯
            used[i] = False
    return

dfs(a, "", 3)
res = [int(i) for i in res]
print(res)
print(len(res))
```

#### 练习02 奖金计算
> 企业发放的奖金根据利润提成。
> 利润(I)低于或等于10万元时，奖金可提10%；
> 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
> 20万到40万之间时，高于20万元的部分，可提成5%；
> 40万到60万之间时高于40万元的部分，可提成3%；
> 60万到100万之间时，高于60万元的部分，可提成1.5%；
> 高于100万元时，超过100万元的部分按1%提成；
> 从键盘输入当月利润I，求应发放奖金总数？

逆向列表
```python
profit = int(input("请输入当月的利润(单位：万元)："))
thresholds = [100, 60, 40, 20, 10, 0]
rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
bonus = 0
for i in range(len(thresholds)):
    if profit > thresholds[i]:
        bonus += (profit - thresholds[i]) * rate[i]
        profit -= profit - thresholds[i]

print("奖金数为：%0.4f万元" % bonus)
```
正向列表

```python
profit = int(input('请输入当月的利润(单位：万元)：'))
bonus = 0
thresholds = [0, 10, 20, 40, 60, 100]
rates = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
for i in range(1, len(thresholds)):
    if profit < thresholds[i]:
        bonus += (profit - thresholds[i-1]) * rates[i-1]
        break
    else:
        bonus += (thresholds[i]-thresholds[i-1]) * rates[i-1]
else:
    bonus += (profit - thresholds[-1]) * rates[-1]

print("奖金数为：%0.4f万元" % bonus)
```
差值列表

```python
profit = int(input('请输入当月的利润(单位：万元)：'))
bonus = 0
thresholds = [10, 10, 20, 20, 40]
rates = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
for i in range(len(thresholds)):
    if profit <= thresholds[i]:
        bonus += profit * rates[i]
        profit = 0
        break
    else:
        bonus += thresholds[i] * rates[i]
        profit -= thresholds[i]
bonus += profit * rates[-1]
print("奖金数为：%0.4f万元" % bonus)
```
#### 练习003 完全平方数

> 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

```python
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
```
#### 练习04 这年第几天

> 输入某年某月某日，判断这一天是这一年的第几天？

```python
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
```
#### 练习05 三数排序
> 输入三个整数x,y,z，请把这三个数由小到大输出。

```python
raw = []
for i in range(1, 4):
    a = int(input("请输入第%d个数:" % i))
    raw.append(a)

j = 0
k = 0
while True:
    for m in range(len(raw)):
        if j == raw[m]:
            print(j， end=' ')
            k += 1
    j += 1
    if k == len(raw):
        break
---------------------------------------
for i in range(len(raw)):
    for j in range(i, len(raw)):
        if raw[i] > raw[j]:
            raw[i], raw[j] = raw[j], raw[i]
print(raw)
```
#### 练习06 养兔子

> 有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

简单解释一下，这个其实就是斐波那契数列，很多程序之所以写错了，其实是因为原则上来说，这个第3月起生一对兔子，指的是第三月月初生一对兔子，而不是月末。

```python
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
```
#### 练习07   100到200的素数

> 判断100-200之间有多少个素数，并输出所有素数。

```python
a = 0
b = []
for i in range(100, 201):
    for j in range(2, int(i**0.5)):
        if i % j == 0:
            break
    else:
        b.append(i)
        a += 1
print("一共有%d个质数" % a)
print(b)
```

#### 练习08 分解质因数
> 将一个正整数分解质因数。例如：输入90,打印出90=2*3\*3\*5

```python
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
print("*".join(b))='')
```
#### 练习09  字符串构成
> 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

```python
a = input("请输入一串字符：")
num = 0
word = 0
character = 0
oth = 0
for i in a:
    if '\u4e00' <= i <= '\u9fef':
        character += 1
    elif '\u0030' <= i <= '\u0039':
        num += 1
    elif '\u0061' <= i <= '\u007a' or '\u0041' <= i <= '\u005a':
        word += 1
    else:
        oth += 1
print("中文字符：%d" % character)
print("英文字符：%d" % word)
print("数字：%d" % num)
print("其他字符：%d" % oth)
```
#### 练习10 叠数相加
> 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

```python
a = input("请输入一个值：")
b = int(input("请输入相加次数："))
c = [int(a*i) for i in range(1, b + 1)]
d = [str(j) for j in c]
print("s=%d=" % sum(c) + '+'.join(d))
```
#### 练习11 完数
> 一个数如果恰好等于它的真因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

```python
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
```
#### 练习12 小球自由落体

> 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
```python
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
```

#### 练习13 乒乓比赛
> 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

```python
m = ['x', 'y', 'z']
for a in m:
    for b in m:
        for c in m:
            if a != b and a != c and b != c:
                if a != 'x' and c != 'x' and c != 'z':
                    print("a的对手是%s，b的对手是%s，c的对手是%s" % (a, b, c))
```
#### 练习14 画菱形
> 打印出以*组成的菱形图案

```python
h = int(input("请输入菱形高度："))
a = h
b = h
for i in range(1, h+1):  # 正三角
    print(" "*(a-1), "*"*(2*i - 1))
    a -= 1
for j in range(1, h):  # 倒三角
    print(" "*j, "*"*(2*b-3))
    b -= 1
```
#### 练习15 反转单词

> 编写一个函数，这个函数将接受一个或多个单词组成的字符串，并对这些单词进行检查，如果大于或等于5个长度，就将它反转，否则不变。传入的字符串仅仅只由单词和空格组成，只有多个单词时才存在空格。例子："Hey fellow warriors" => "Hey wollef sroirraw"； "This is a test" => "This is a test"；"This is another test" => "This is rehtona test"
```python
def spin_words(sentence):
    a = sentence.split()
    for i in range(len(a)):
        if len(a[i]) >= 5:
            a[i] = a[i][::-1]
    string = " ".join(a)
    return string
```
#### 练习16 列表过滤
> 编写一个函数，这个函数将接受一个带有数字和字符串的列表，对这个列表进行过滤操作，移除字符串，返回只有数字的列表。
> 例子：
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
```python
def filter_list(l):
    new = []
    for i in l:
        if not isinstance(i, str):
            new.append(i)
    return new
```
#### 练习17 数字游戏
> 编写一个函数，接收两个正整数n和p，其中n写作abcd...， 其中a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) +... = n * k，如果k存在，返回k的值，否则返回-1.
> 例子：
> 89 --> 8¹ + 9² = 89 * 1（n=89，p=1）
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2（n=695，p=2 ）
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51（n=46288，p=3）

```python
def dig_pow(n, p):
    a = [int(i) for i in str(n)]
    s = 0
    for j in range(len(a)):
        s += a[j] ** (p + j)
    return s // n if s % n == 0 else -1
```
#### 练习18 字母转换
> 将字母转换为它在字母表中的位置，忽略其他的符号。
> 例子："The sunset sets at twelve o' clock."
> 转换："20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
> 返回值是字符串。

```python
def alphabet_position(text):
        a = [i for i in text.lower()]
        b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
             'y', 'z']
        return ' '.join([str(k + 1) for j in a for k in range(len(b)) if j == b[k]])
        # 用一行写完
        # return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
```
#### 练习19 Persistent Bugger
> Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
> 简单解释一下，就是写一个函数，这个函数将接受一个正整数，然后将组成这个正整数的数字连续相乘，直到最后结果是一个一位数。返回相乘次数。
> 例子：
输入39，3*9=27，2\*7=14，1\*4=4，输出3
输入4，输出0
输入999，9\*9\*9=729，7\*2\*9=126，1\*2\*6=12，1\*2=2，输出4

```python
def persistence(n):
    count = 0
    while len(str(n)) > 1:
        s = 1
        for j in str(n):
            s *= int(j)
        count += 1
        n = str(s)
    return count
```
#### 练习20 Pick peaks 寻找极值

> 编写一个函数，这个函数将接受一个整数列表，找到这个列表中所有极值，返回一个字典，这个字典包含所有极值的位置和值。
> 要求：当出现连续几个相等的极值时，返回第一个的位置和值即可。
> 即[1, 2, 2, 2, 3]，返回{'pos': [1], 'peaks':[2]}(第一个是它的位置，第二个是值) 
> 极值不会出现在列表的顶端和末尾。 [1, 2, 2, 2, 3]和[1, 2, 2, 2,2]没有极值。

```python
def pick_peaks(arr):
    pos, peak = [], []
    dic = {"pos": [], "peaks": []}
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            peak, pos = [arr[i]], [i]
        elif arr[i] < arr[i - 1]:
            dic["peaks"] += peak
            dic["pos"] += pos
            peak, pos = [], []
    return dic
```
