h, w = map(int, input().split())
ans = 0
for i in range(h):
    a = list(map(str, input()))
    for k in range(w):
        if str.isdecimal(a[k]):
            ans += int(a[k])

print(ans)