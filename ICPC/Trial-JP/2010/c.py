import sys
import itertools
input = sys.stdin.readline

inf = 10 ** 20
a = [i ** 2 for i in range(256)]
ML = list(range(256))
def f(n, m):
    c = [int(input()) for i in range(m)]
    x = [int(input()) for i in range(n)]
    dp = [inf] * 256
    dp[128] = 0
    ck = list(map(lambda x: (max(min(x[0]+x[1], 255), 0), x[1]), (itertools.product(c, ML))))
    for i in range(n):
        xi = x[i]
        ndp = [inf] * 256
        for nk, k in ck:
            if ndp[nk] > dp[k]:
                ndp[nk] = dp[k]
        dp = [nn + a[abs(xi - i)] for i, nn in enumerate(ndp)]
    return min(dp)a[abs(xi-i)]

if __name__ == "__main__":
    while 1:
        n, m = map(int, input().split())
        if n == 0 and m == 0: break
        print(f(n,m))