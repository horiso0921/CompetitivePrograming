n, L, R = map(int, input().split())
a = list(map(int, input().split()))

ans = []

for i in range(n):
    if a[i] < L:
        ans.append(L)
    elif a[i] > R:
        ans.append(R)
    else:
        ans.append(a[i])

for i in range(n):
    print(ans[i], end=" ")