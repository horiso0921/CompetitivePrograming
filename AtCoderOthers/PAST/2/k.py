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
    n = II()
    s = S()
    c = LI()
    d = LI()
    dp = [[inf] * (n+1) for i in range(n)]
    if s[0] == "(":
        dp[0][0] = d[0]
        dp[0][1] = 0
    else:
        dp[0][0] = d[0]
        dp[0][1] = c[0]
    for i in range(1, n):
        if s[i] == "(":
            dp[i][0] = min(dp[i - 1][0] + d[i], dp[i - 1][1] + c[i])
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + d[i], dp[i - 1][j + 1] + c[i])
        else:
            dp[i][0] = min(dp[i - 1][0] + d[i], dp[i - 1][1])
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j + 1], dp[i - 1][j] + d[i], dp[i - 1][j - 1] + c[i])
    print(dp[-1][0])
    return


#main
if __name__ == '__main__':
    solve()
