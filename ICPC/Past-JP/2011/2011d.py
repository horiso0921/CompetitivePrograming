def main(n):
    a = list(map(int, input().split()))
    dp = [[0] * n for i in range(n)]
    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) <= 1:
            dp[i][i + 1] = 2
    for i in range(2, n):
        for l in range(n - i):
            r = i + l
            res = 0
            if abs(a[l] - a[r]) <= 1:
                if dp[l + 1][r - 1] == r - l - 1:
                    dp[l][r] = r - l + 1
                    continue
            res = dp[l + 1][r - 1]
            for li in range(l + 1, r):
                tmp = dp[l][li] + dp[li + 1][r]
                if res < tmp:
                    res = tmp
            dp[l][r] = res
    print(dp[0][n-1])
    def dfs(l, r):
        if l >= r: return 0
        if dp[l][r] != -1: return dp[l][r]
        if abs(a[l] - a[r]) <= 1:
            if dfs(l + 1, r - 1) == r - l - 1:
                dp[l][r] = r - l + 1
                return r - l + 1
        res = 0
        for li in range(l + 1, r):
            tmp = 0
            f = 0
            if dp[l][li] != -1:
                tmp += dp[l][li]
            else:
                tmp += dfs(l, li)
            if dp[li + 1][r] != -1:
                tmp += dp[li + 1][r]
            else:
                tmp += dfs(li + 1, r)
            if res < tmp:
                res = tmp
        dp[l][r] = res
        return res
    # print(dfs(0, n - 1))


if __name__ == "__main__":
    while 1:
        n = int(input())
        if n:
            main(n)
        else:
            break
