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
inf = float('INF')

#solve
def solve():
    n, l = LI()
    x = LI() + [inf]
    t = LI()
    dp = [inf] * (l + 4)
    j = 0
    dp[0] = 0
    for i in range(l):
        if x[j] == i:
            dp[i] += t[2]
            j += 1
        dp[i + 1] = min(dp[i + 1], dp[i] + t[0])
        dp[i + 2] = min(dp[i + 2], dp[i] + t[0] + t[1])
        dp[i + 4] = min(dp[i + 4], dp[i] + t[0] + 3 * t[1])
    print(min(dp[l]
            , dp[l - 1] + t[0] // 2 + t[1] // 2
            , dp[l - 2] + t[0] // 2 + t[1] // 2 * 3
            , dp[l - 3] + t[0] // 2 + t[1] // 2 * 5 ))
    return


#main
if __name__ == '__main__':
    solve()
