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
def IR(n):
    res = [None] * n
    for i in range(n):
        res[i] = II()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI()
    return res
def FR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR_(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI_()
    return res
def SR(n):
    res = [None] * n
    for i in range(n):
        res[i] = S()
    return res
def LSR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LS()
    return res
mod = 998244353
inf = float('INF')

#solve
def solve():
    n, m = LI()
    fact = [i for i in range(m + 1)]
    fact[0] = 1
    for i in range(m):
        fact[i + 1] *= fact[i]
        fact[i + 1] %= mod
    invfact = [None] * (m + 1)
    invfact[m] = pow(fact[m], mod - 2, mod)
    for i in range(m - 1, 0, -1):
        invfact[i] = invfact[i + 1] * (i + 1)
        invfact[i] %= mod
    def com(n, k):
        if n < 0 or k < 0 or n < k: return 0
        if n == 0 or k == 0 or n == k: return 1
        return (fact[n] * invfact[k] * invfact[n - k]) % mod
    ans = com(m, n - 1)
    tmp = 0
    for i in range(1, n - 1):
        tmp += com(n - 2, i) * i
        tmp %= mod
    ans = ans * tmp % mod
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
