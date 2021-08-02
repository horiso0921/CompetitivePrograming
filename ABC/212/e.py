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
mod = 998244353
inf = 1e10

#solve
def solve():
    n,m,k = LI()
    edg = [[i] for i in range(n)]
    for _ in range(m):
        u,v = LI_()
        edg[u].append(v)
        edg[v].append(u)
    dp = [[0] * n for i in range(k+1)]
    dp[0][0] = 1
    for i in range(k):
        tmp = 0
        for j in range(n):
            kj = dp[i][j]
            tmp += kj
            for e in edg[j]:
                dp[i+1][e] -= kj
        for j in range(n):
            dp[i+1][j] += tmp
            dp[i+1][j] %= mod
    print(dp[-1][0])

    return


#main
if __name__ == '__main__':
    solve()