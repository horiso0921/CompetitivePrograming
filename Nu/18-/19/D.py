N, K = map(int, input().split())
D = list(map(int, input().split()))

while 1:
    n = list(str(N))
    for i in range(len(n)):
        if int(n[i]) in D:
            N += 1
            break
    else:
        print(N)
        break