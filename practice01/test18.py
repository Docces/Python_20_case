def alphabet_position(text):
        a = [i for i in text.lower()]
        b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
             'y', 'z']
        return ' '.join([str(k + 1) for j in a for k in range(len(b)) if j == b[k]])

        # 用一行写完
        # return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
