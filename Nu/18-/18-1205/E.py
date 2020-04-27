m, n, N = map(int, input().split())
ans = N
amari = 0
while ((N + amari) // m) > 0:
    amari1 = (N + amari) % m
    N = ((N + amari) // m) * n
    amari = amari1
    ans += N
print(ans)