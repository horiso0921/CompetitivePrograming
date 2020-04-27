n, m = map(int, input().split())

dp = [[0 for k in range(m+1)] for i in range(n+1)]
a = []

for i in range(n):
    a.append(int(input()))
a.sort()

for i in range(n):
    for j in range(m+1):
        if j < a[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - a[i]] + a[i])
print(dp[n][m])