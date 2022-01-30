#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
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
    n,k = LI()
    a = LI()
    a[0] -= k
    for ai in a[1:]:
        a[0] -= ai
    if a[0] < 0:
        print(0)
        return
    div = [i for i in range(201)]
    div[0] = 1
    for i in range(200):
        div[i+1] *= div[i]
        div[i+1] %= mod
    for i in range(201):
        div[i] = pow(div[i], mod-2, mod)
    def f(n,k):
        if n == 0: return 1
        if k == 0: return 1
        if n == k: return 1
        res = 1
        for i in range(n, n-k, -1):
            res *= i
            res %= mod
        res *= div[k]
        return res % mod
    ans = 1
    for ai in a:
        ans *= f(ai+k-1, k-1)
        ans %= mod
    print(ans % mod)
    
    return


#main
if __name__ == '__main__':
    solve()