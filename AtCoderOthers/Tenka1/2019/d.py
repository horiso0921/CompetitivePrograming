#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 998244353
inf = 1e10

#solve
def solve():
    n = II()
    ans = pow(3, n, mod)
    p = [pow(2, i, mod) for i in range(n + 1)]
    a = IR(n)
    a.sort()
    acc = list(itertools.accumulate(a))
    dp = [[0] * (acc[-1] + 1) for i in range(n + 1)]
    dp[0][0] = 1
    for i, ai in enumerate(a):
        for j in range(i + 1, 0, -1):
            for k in range(acc[i], ai - 1, -1):
                dp[j][k] += dp[j - 1][k - ai]
                dp[j][k] %= mod

    for i in range(1, n + 1):
        for j in range((acc[-1] - 1) // 2 + 1, acc[-1] + 1):
            ans -= dp[i][j] * p[n - i] * 3
            ans %= mod
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
