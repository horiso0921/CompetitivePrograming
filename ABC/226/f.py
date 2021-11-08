#!/usr/bin/env python3
from functools import lru_cache
from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys
import itertools
import math
sys.setrecursionlimit(10**6)
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

fn = [i for i in range(51)]
fn[0] = 1
for i in range(50):
    fn[i+1] *= fn[i]
    fn[i+1] %= mod


def combination_mod(n, k, mod):
    """ power_funcを用いて(nCk) mod p を求める """
    """ nCk = n!/((n-k)!k!)を使用 """
    if n < 0 or k < 0 or n < k:
        return 0
    if n == 0 or k == 0:
        return 1
    a = fn[n] % mod
    b = fn[k] % mod
    c = fn[n - k] % mod
    return (a * pow(b, mod - 2, mod) * pow(c, mod - 2, mod)) % mod


@lru_cache(maxsize=10**6)
def dfs(i, j):
    if j == 1:
        return 1
    if i == 0:
        return 1
    res = 0
    for xi in range(1, min(j, i+1)):
        if xi == 1:
            res += 1
        else:
            tmp = 1
            for j in range(1, i // xi + 1):
                tmp *= pow(xi, mod-2, mod)
                res += tmp * dfs(i - xi * j, xi) * \
                    fn[i] * pow(fn[i-j*xi], mod-2, mod) % mod
                res %= mod
        res %= mod
    return res

# solve


def solve():
    n, k = LI()
    ans = 0
    for i in range(1, n+1):
        if i == 1:
            ans += 1
        else:
            tmp = 1
            for j in range(1, n // i + 1):
                tmp *= pow(i, mod-2, mod)
                ans += tmp * \
                    dfs(n - i * j, i) * fn[i] * pow(fn[n-i*j],
                                                    mod-2, mod) * pow(i, k, mod) % mod
                ans %= mod
            print(tmp * dfs(n - i * j, i) * fn[i] * pow(fn[n-i*j], mod-2, mod) % mod)
    print(ans)
    return


# main
if __name__ == '__main__':
    solve()
