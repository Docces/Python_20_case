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
