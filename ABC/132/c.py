
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
def C():
    n = II()
    d = LI()
    d.sort()
    ans = 0
    for i in range(10**5+1):
        if n // 2 == bisect_left(d, i):
            ans += 1
    print(ans)
    return


def combination_mod(n, k, mod):
    # power_funcを用いて(nCk) mod p を求める 
    # nCk = n!/((n-k)!k!)を使用

    from math import factorial
    if n < 0 or k < 0 or n < k: return 0
    if n == 0 or k == 0: return 1
    a = factorial(n) % mod
    b = factorial(k) % mod
    c = factorial(n - k) % mod
    return (a * power_func(b, mod - 2, mod) * power_func(c, mod - 2, mod)) % mod
    
def power_func(a, b, mod):
    # a^b mod p を求める
    # bを2進数分解して高速累乗

    if b == 0: return 1
    if b % 2 == 0:
        d = power_func(a, b // 2, mod)
        return d * d % mod
    if b % 2 == 1:
        return (a * power_func(a, b - 1, mod)) % mod

