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
mod = 1000000007
inf = 1e10

fact = [i for i in range(2 * 10 ** 5+ 1)]
fact[0] = 1
for i in range(2 * 10 ** 5):
    fact[i+1] *= fact[i]
    fact[i+1] %= mod

def factorial(n):
    return fact[n]


def combination_mod(n, k, mod):
    """ power_funcを用いて(nCk) mod p を求める """ 
    """ nCk = n!/((n-k)!k!)を使用 """
    if n < 0 or k < 0 or n < k: return 0
    if n == 0 or k == 0: return 1
    a = factorial(n) % mod
    b = factorial(k) % mod
    c = factorial(n - k) % mod
    return (a * pow(b, mod - 2, mod) * pow(c, mod - 2, mod)) % mod

#solve
def solve():
    n = II()
    c = LI()
    c.sort()
    ans = 1
    t = 0
    for i in c:
        ans *= i - t if i - t > 0 else 0
        t += 1
        ans %= mod
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()