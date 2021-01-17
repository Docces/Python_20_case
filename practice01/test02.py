# 逆向列表
profit = int(input("请输入当月的利润(单位：万元)："))
thresholds = [100, 60, 40, 20, 10, 0]
rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
bonus = 0
for i in range(len(thresholds)):
    if profit > thresholds[i]:
        bonus += (profit - thresholds[i]) * rate[i]
        profit -= profit - thresholds[i]

print("奖金数为：%0.4f万元" % bonus)

# 正向列表
profit = int(input('请输入当月的利润(单位：万元)：'))
bonus = 0
thresholds = [0, 10, 20, 40, 60, 100]
rates = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
for i in range(1, len(thresholds)):
    if profit < thresholds[i]:
        bonus += (profit - thresholds[i - 1]) * rates[i - 1]
        break
    else:
        bonus += (thresholds[i] - thresholds[i - 1]) * rates[i - 1]
else:
    bonus += (profit - thresholds[-1]) * rates[-1]

print("奖金数为：%0.4f万元" % bonus)

# 差值列表
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
