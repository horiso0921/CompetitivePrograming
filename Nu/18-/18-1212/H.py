C = input()
a = C + C + C
b = list(C + C + C)
c = list(a)
d = list(a)
ans = 0

    for i in range(len(C)):
        for k in range(len(C) * 2):
            if a[i + k] == "x" and c[k] == "o":
                b[i + k] = "o"
        if i == 0:
            d = b
        elif b.count("o") > d.count("o"):
            d = b
        else:
            continue
    