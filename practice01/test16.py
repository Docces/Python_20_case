def filter_list(l):
    new = []
    for i in l:
        if not isinstance(i, str):
            new.append(i)
    return new


a = [12, 23, 34, "123", "www", "wee"]
print(filter_list(a))
