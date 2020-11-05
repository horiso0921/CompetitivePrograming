import sys
sys.setrecursionlimit(10 ** 8)
inf = float("INF")
n,k = map(int, input().split())
dp = [inf] * n
xw = [[int(i) for i in input().split()] for j in range(n)]
lsum = [[inf] * n for i in range(n)]
rsum = [[inf] * n for i in range(n)]
for i in range(n):
    res = 0
    weight = 0
    xi,wi = xw[i]
    lsumi = lsum[i]
    for j in range(i, n):
        xj,wj = xw[j]
        res += (weight + 1) * (xj - xi)
        lsumi[j] = res
        weight += wj
        xi = xj

for i in range(n-1,-1,-1):
    res = 0
    weight = 0
    xi,wi = xw[i]
    for j in range(i, -1, -1):
        xj,wj = xw[j]
        res += (weight + 1) * (xi - xj)
        rsum[j][i] = res
        weight += wj
        xi = xj


for i in range(n):
    tmp = inf
    for j in range(i):
        x = dp[j] + 
print(dfs(0,n-1))
