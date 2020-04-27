N, C, K = map(int, input().split())

T = [int(input()) for i in range(N)]

T.sort()
A = T[0]
SUM = 1
ans = 0
for i in range(1, N):
    SUM += 1
    if T[i] - A > K:
        ans += 1
        SUM = 1
        A = T[i]
    elif SUM > C:
        ans += 1
        SUM = 1
        A = T[i]

        
print(ans+1)
    