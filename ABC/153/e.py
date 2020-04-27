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
def solve():
    h, n = LI()
    ab = LIR(n)
    maxa = max(map(lambda x: x[0], ab))
    rangeh = h + maxa
    dp = [inf] * (rangeh + 1)
    dp[0] = 0
    for a,b in ab:
        for hi in range(rangeh - a):
            dp[hi + a] = min(dp[hi + a], dp[hi] + b)
        for hi in range(rangeh-1, -1, -1):
            dp[hi] = min(dp[hi], dp[hi + 1])
    print(dp[h])
    return


#main
if __name__ == '__main__':
    solve()
