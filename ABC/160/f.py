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
fact = [i for i in range(2 * 10 ** 5 + 1)]
fact[0] = 1
for i in range(1,2 * 10 ** 5 + 1):
    fact[i] *= fact[i - 1]
    fact[i] %= mod

def combination_mod(n, k, mod):
    """ power_funcを用いて(nCk) mod p を求める """
    """ nCk = n!/((n-k)!k!)を使用 """
    from math import factorial
    if n < 0 or k < 0 or n < k:
        return 0
    if n == 0 or k == 0:
        return 1
    a = fact[n]
    b = fact[k]
    c = fact[n - k]
    return (a * pow(b, mod - 2, mod) * pow(c, mod - 2, mod)) % mod
#solve
def solve():
    n = II()
    ab = LIR_(n - 1)
    edg = [[] for i in range(n)]
    for a, b in ab:
        edg[a].append(b)
        edg[b].append(a)
    rank = [-1] * n
    rank[0] = 0
    dp0 = [1] * n
    dp1 = [1] * n
    dp2 = [1] * n
    dp3 = [1] * n
    def dfs1(p, pre=-1):
        rank[p] = rank[pre] + 1
        for e in edg[p]:
            if e != pre:
                dfs1(e, p)
                dp0[p] += dp0[e]
                dp2[p] *= dp2[e] * combination_mod(dp0[p] - 1, dp0[e], mod)
                dp2[p] %= mod
    fact = [i for i in range(n)]
    fact[0] = 1
    for i in range(1, n):
        fact[i] *= fact[i - 1]
        fact[i] %= mod
    dfs1(0)
    print(dp2[0])
    def dfs2(p, pre=-1):
        if dp3[p] != 1:
            return dp3[p]
        if p == 0:
            return 
        for e in edg[p]:
            if e != pre:
                print(e)
                if rank[e] == rank[p] + 1:
                    dp1[p] += dp0[e]
                    dp3[p] *= dp2[e] * combination_mod(dp1[p] - 1, dp0[e], mod)
                else:
                    dfs2(e, p)
                    dp1[p] += dp1[e]
                    dp3[p] *= dp3[e] * combination_mod(dp1[p] - 1, dp1[e], mod)
                dp3[p] %= mod
        if pre == -1:
            for e in edg[p]:
                if rank[e] == rank[p] - 1:
                    return dp2[p] * dp3[e] * combination_mod(n - 1, dp1[e], mod)
    print(dp0)
    print(dp1)
    print(dp2)
    print(dp3)
    for i in range(1, n):
        print(dfs2(i))
        print(dp0)
        print(dp1)
        print(dp2)
        print(dp3)
    

    return


#main
if __name__ == '__main__':
    solve()
