#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    x, y = LI()
    if x < y:
        print("Better")
    else:
        print("Worse")
    return

#B
def B():
    n = II()
    print(n + (1 * (n % 2) or -1))
    return

#C
def C():
    def power_func(a, b, mod):
        if b == 0: return 1
        if b & 1 == 0:
            d = power_func(a, b // 2, mod)
            return d * d % mod
        if b & 1 == 1:
            return (a * power_func(a, b - 1, mod)) % mod

    def combination_mod(n, k, mod):
        from math import factorial
        if n < 0 or k < 0 or n < k: return 0
        if n == 0 or k == 0: return 1
        a = factorial(n) % mod
        b = factorial(k) % mod
        c = factorial(n - k) % mod
        return (a * power_func(b, mod - 2, mod) * power_func(c, mod - 2, mod)) % mod
    a,b = LI()
    print(combination_mod(a + b - 2, a - 1, mod))
    return

# D
# 解説AC
# 塩何グラムが必要かで優先度をつけられるとかわからんやん
def D():
    def f(mid):
        res = []
        for num, wpi in enumerate(wp):
            w, p = wpi
            res.append((w * (mid - p), num))
        res.sort()
        tmp = [0,0]
        for i in range(k):
            w, p = wp[res[i][1]]
            tmp[0] += w
            tmp[1] += w * p
        if tmp[1] / tmp[0] >= mid:
            return True
        return False
    n, k = LI()
    wp = LIR(n)
    ok = 0
    ng = 100
    for _ in range(100):
        mid = (ok + ng) / 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    print(mid)
#Solve
if __name__ == '__main__':
    D()
