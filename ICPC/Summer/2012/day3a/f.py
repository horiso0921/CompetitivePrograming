n = int(input())
dp = [0] * (n+2)
mod = 10 ** 9 + 7
dp[0] = 1
for i in range(n):
    ndp = [0] * (n+2)
    c = input().rstrip()
    if c == "-":
        for j in range(n):
            ndp[j+1] = dp[j]
    elif c == "U":
        for j in range(n):
            ndp[j+1] += dp[j] * (i-j)
            ndp[j] += dp[j]
    elif c == "D":
        for j in range(n):
            ndp[j+2] += dp[j] * (i-j) ** 2
            ndp[j+1] += dp[j] * (i-j)
    dp = [i % mod for i in ndp]

print(dp[n])