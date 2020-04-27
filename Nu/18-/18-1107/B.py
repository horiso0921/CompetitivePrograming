N = int(input())

for i in range(N):
    a = list(map(int, input().split()))
    if(i == 0):
        mx = a[0]
        my = a[0]
        mi = a[1]
    else:
        if(my < a[0]):
            my = a[0]
            mi = a[1]


score = my
score += mi
print(score)