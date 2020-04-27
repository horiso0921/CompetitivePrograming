N = int(input())

P = [int(input()) for i in range(N)]

for i in range(10):
    for k in range(N):
        if(P[k]%10**i == 0):
            continue
        else:
            print(i-1)
            quit()
print(9)
    