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
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')


def combination_mod(n, k, mod):
    """ power_funcを用いて(nCk) mod p を求める """
    """ nCk = n!/((n-k)!k!)を使用 """
    from math import factorial
    if n < 0 or k < 0 or n < k:
        return 0
    if n == 0 or k == 0:
        return 1
    a = factorial(n) % mod
    b = factorial(k) % mod
    c = factorial(n - k) % mod
    return (a * pow(b, mod - 2, mod) * pow(c, mod - 2, mod)) % mod
#solve
def solve():
    n, k = LI()
    if n > k:
        print(combination_mod(n + k - 1, n - 1, mod))
        return
    dp = [[[0, 0]] * (k + 1) for i in range(n)]
    dp0 = dp[0]
    for i in range(k + 1):
        dp0[i] = [i, 1]
    for i in range(1, n):
        dpi = dp[i]
        dpi1 = dp[i - 1]
        for j in range(k + 1):
            tmp = [0, 0]
            for l in range(j + 1):
                if tmp[0] < dpi1[l][0] * (j - l):
                    tmp = [dpi1[l][0] * (j - l), dpi1[l][1]]
                elif tmp[0] == dpi1[l][0] * (j - l):
                    tmp[1] += dpi1[l][1]
                    tmp[1] %= mod
            dpi[j] = tmp
    print(dp[-1][-1][-1])

    return


#main
if __name__ == '__main__':
    solve()
