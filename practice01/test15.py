def spin_words(sentence):
    a = sentence.split()
    for i in range(len(a)):
        if len(a[i]) >= 5:
            a[i] = a[i][::-1]
    string = " ".join(a)
    return string


print(spin_words("welcome"))
