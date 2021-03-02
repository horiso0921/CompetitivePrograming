def main(s1):
    s2 = input()
    a, e, s, r = [int(input()) for i in range(4)]
    s = min(s, a + e)
    r = min(r, a + e)
    
    n,m = len(s1),len(s2)
    ans = float("INF")
    pres1 = s1
    for k in range(n):
        s1 = pres1[k:]+pres1[:k]
        b = k * r
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = dp[i-1][0]+e
            if i - 1 >= n - k:
                dp[i][0] -= r
        for j in range(m+1):
            dp[0][j] = j * a
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                cost = 0 if s1[i - 1] == s2[j - 1] else s
                cost1 = e - r if i - 1 >= n - k else e
                dp[i][j] = min(dp[i - 1][j] + cost1,
                                dp[i][j - 1] + a,
                                dp[i - 1][j - 1] + cost)

        ans = min(ans,dp[n][m]+b)
    print(ans)
while 1:
    s = input()
    if s == "#":
        break
    main(s)