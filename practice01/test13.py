m = ['x', 'y', 'z']
for a in m:
    for b in m:
        for c in m:
            if a != b and a != c and b != c:
                if a != 'x' and c != 'x' and c != 'z':
                    print("a的对手是%s，b的对手是%s，c的对手是%s" % (a, b, c))
