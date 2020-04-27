#A
"""
H, W = map(int, input().split())
h, w = map(int, input().split())
print(H*W-h*W-w*H+h*w)
"""
#B
"""
n, m, c = map(int, input().split())
b = list(map(int, input().split()))
ans = 0
ansb = 0
for i in range(n):
    ans = 0
    a = list(map(int, input().split()))
    for k in range(m):
        ans += a[k]*b[k]
    ans += c
    if ans > 0:
        ansb += 1
print(ansb)
"""
#C
"""
n, m = map(int, input().split())
ans = []
ansnum = 0
honsuu = 0
for i in range(n):
    a = list(map(int, input().split()))
    ans.append(a)
ans.sort()
for i in ans:
    if honsuu + i[1] <= m:
        ansnum += i[0] * i[1]
        honsuu += i[1]
    else:
        ansnum += (m - honsuu) * i[0]
        break

print(ansnum)
"""
# D
# 解説AC
# わかるかぼけ
# F(a,b) = F(0,a-1)^F(0,B)
a, b = map(int, input().split())
def F(x):
    tmp1, tmp2 = (x+1) >> 1, x & 1
    rast = 0 if tmp2 else x
    fast = tmp1 & 1
    return rast ^ fast
print(F(a - 1) ^ F(b))