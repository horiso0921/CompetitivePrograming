N,M = map(int, input().split())

if(N == 1 or M == 1):
    if(M == 1 and N == 1):
        print(1)
    else:
        print(max(M-2, N-2))
else:
    print((N-2)*(M-2))
