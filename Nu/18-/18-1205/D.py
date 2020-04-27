N, M, A, B = map(int, input().split())
flg = 0
if N <= A:
    N += B
for i in range(M):
    c = int(input())
    N = N - c
    if N < 0:
        flg = i+1
        break
    elif N <= A:
        N = N + B
if flg != 0:
    print(flg)
else:
    print("complete")

