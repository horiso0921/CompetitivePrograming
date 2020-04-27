N = int(input())
ansm = 0
for i in range(N):
    if i == 0:
        k = int(input())
        ansm = k
        ansmi = k
    elif i == 1:
        l = int(input())
        ansm += l
        lkmin = abs(l - k)
        ansmi = lkmin
        lkminck = 1
    else:
        x = int(input())
        if ansmi - x < 0 and lkminck:
            lkminck = 0
            ansmi = 0
        if ansm - x < 0:
            ansmi = abs(ansm - x)
            lkmin = ansmi
            lkminck = 1
        elif ansmi > 0:
                ansmi -= x
        ansm += x
print(ansm)
print(ansmi)          