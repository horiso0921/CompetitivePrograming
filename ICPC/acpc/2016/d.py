T = int(input())
n = int(input())
st = [[int(i) for i in input().split()] for i in range(n)]
ans = 0
r = 0
tmp = 0
for l in range(n):
    tmps, tmpt = st[l]
    for r in range(r, n):
        rs, rt = st[r]
        if rs >= tmps + T:
            ans = max(ans, tmp)
            break
        if rs <= tmps + T <= rt:
            ans = max(ans, tmp + T + tmps - rs)
            break
        tmp += rt - rs
    else:
        ans = max(ans, tmp)
    tmp -= tmpt - tmps
tmp = 0
st = st[::-1]
r = 0
for l in range(n):
    tmps, tmpt = st[l]
    for r in range(r, n):
        rs, rt = st[r]
        if rt <= tmpt - T:
            ans = max(ans, tmp)
            break
        if rs <= tmpt - T <= rt:
            ans = max(ans, tmp + rt - (tmpt - T))
            break
        tmp += rt - rs
    ans = max(ans, tmp)
    tmp -= tmpt - tmps

print(ans)