def main(n, m):
    dp = [(i + 1) for i in range(n)]
    dp = dp[::-1]
    for _ in range(m):
        p, c = map(int, input().split())
        dp = dp[p - 1:p + c - 1] + dp[:p - 1] + dp[p + c - 1:]
    print(dp[0])
while 1:
    n, r = map(int, input().split())
    if n == r == 0:
        break
    main(n,r)