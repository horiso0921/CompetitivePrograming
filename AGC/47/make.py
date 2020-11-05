print(2 * 10 ** 5)
ans = []
nd = [chr(ord("a") + i) for i in range(26)]
x = [chr(ord("a") + i) for i in range(26)]
for i in nd:
    print(i)
i = 26
z = 26
while 1:
    tmp = []
    for l in nd:
        for a in x:
            i += len(l) + 1
            if i >= 10 ** 6 or z == 2 * 10 ** 5:
                exit()
            o = l + a
            print(o)
            z += 1
            tmp.append(l + a)
    nd = tmp