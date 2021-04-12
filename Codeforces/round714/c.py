# solve
def solve():
    import sys
    input = sys.stdin.readline
    mod = 1000000007
    t = int(input())
    dp = [None] * (2 * 10 ** 5 + 10)
    dp[0] = [0] * 10
    dp[0][0] = 1
    dpi = dp[0]
    dpc = [0] * (2 * 10 ** 5 + 10)
    dpc[0] = 1
    for i in range(2 * 10 ** 5 + 9):
        dpi1 = [dpi[9]] + dpi[:-1]
        dpi1[1] = (dpi[0] + dpi[9]) % mod
        dpc[i + 1] = (dpc[i] + dpi[9]) % mod
        dpi = dpi1
        dp[i + 1] = dpi1
    alis = [None] * t
    for i in range(t):
        n, m = input().split()
        m = int(m)
        ans = 0
        for ni in n:
            ans += dpc[m + int(ni)]
            if ans >= mod:
                ans %= mod
        alis[i] = str(ans)
    print("\n".join(alis))
    return
# main
if __name__ == '__main__':
    solve()
