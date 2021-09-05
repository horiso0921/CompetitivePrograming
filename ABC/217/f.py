#!/usr/bin/env python3
from collections import defaultdict
import sys, random
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
def LI(): return list(map(int, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
mod = 998244353
import pprint

printt = pprint.pprint

n,m = LI()
ab = [[0] * (2 * n) for i in range(2 * n)]
for _ in range(m):
    a,b = LI_()
    # a,b = [random.randint(0, 2*n-1), random.randint(0, 2*n-1)]
    ab[a][b] = 1
    ab[b][a] = 1
dp = [[1 if i >= j else 0 for j in range(2*n+1)] for i in range(2*n)]

fact = [i for i in range(300)]
fact[0] = 1
for i in range(299):
    fact[i+1] *= fact[i]
    fact[i+1] %= mod

inv = list(map(lambda x: pow(x, mod-2, mod),fact))

def combination_mod(n, k, mod):
    a = fact[n] * inv[k]
    a %= mod
    return (a * inv[n-k]) % mod
for h in range(2, 2 * n + 2, 2):
    for l in range(2 * n - h + 1):
        r = l + h
        if h == 2:
            if ab[l][r - 1]:
                dp[l][r] = 1
            continue
        res = 0
        if ab[l][r - 1]:
            res = dp[l+1][r-1]

        j = 0
        for i in range(l+2, r, 2):
            j += 1
            if ab[l][i-1]:
                tmp = dp[l+1][i-1] * dp[i][r]
                tmp %= mod
                tmp *= combination_mod(h // 2, j, mod)
                # printt(dp)
                tmp %= mod
                res += tmp
                res %= mod
        dp[l][r] = res
print(dp[0][n*2])
