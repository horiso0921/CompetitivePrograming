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
    a, b, c, k = LI()
    s, t = LI()
    if s + t >= k:
        print((a - c) * s + (b - c) * t)
    else:
        print(a * s + b * t)
        
    return

#B
def B():
    n, t = LI()
    ans = 0
    b = II()
    for _ in range(n-1):
        x = II()
        if x - b >= t:
            ans += t
            b = x
        else:
            ans += x - b
            b = x
    print(ans+t)
    return

#C
def C():
    _, d, k = LI()
    lr = LIR(d)
    for _ in range(k):
        s, t = LI()
        t0 = s
        t1 = s
        for num, lri in enumerate(lr):
            l, r = lri
            if t0 <= r and t1 >= l:
                if t0 > l:
                    t0 = l
                if t1 < r:
                    t1 = r
            if t0 <= t <= t1:
                print(num+1)
                break
    return

#D
def D():
    def power_func(a, b, mod):
        """ a^b mod p を求める """
        """ bを2進数分解して高速累乗 """

        if b == 0: return 1
        if b % 2 == 0:
            d = power_func(a, b // 2, mod)
            return d * d % mod
        if b % 2 == 1:
            return (a * power_func(a, b - 1, mod)) % mod
    a,b,c = IR(3)
    r = (b * c % mod - a * c % mod) * power_func(a * b - b * c + a * c, mod - 2, mod) % mod
    c = (b * c % mod - a * b % mod) * power_func(a * c - b * c + a * b, mod - 2, mod) % mod
    print(r, c)
    return

#Solve
if __name__ == '__main__':
    D()
