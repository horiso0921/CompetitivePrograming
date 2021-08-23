
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

#solve
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

