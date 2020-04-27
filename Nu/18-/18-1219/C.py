n, m = map(int, input().split())
ans = -1
n -= m
if n == 0:
    print(0)
else:
    ans = n // (m + 1)
    if n % (m + 1) == 0:
        print(ans)
    else:
        print(ans+1)