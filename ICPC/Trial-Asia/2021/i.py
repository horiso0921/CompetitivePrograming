#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop, heapify
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
mod = 1000000007
inf = 1e10

#solve
def solve():
    s,n = LI()
    ah = LIR(s)
    ah.sort(key=lambda x:x[1])
    dp = [[0] * n for i in range(s)]
    dp[0][1] = ah[0][0] + ah[0][1]
    for i in range(s-1):
        dp[i+1][1] = max(dp[i][1], ah[i+1][0] + ah[i+1][1])
    for i in range(1, s):
        for j in range(1, n-1):
            dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j] + ah[i][0])
    ans = 0
    for i in range(1, s):
        ans = max(ans, dp[i-1][-1] + ah[i][0] - ah[i][1])

    print(ans)
    return


#main
if __name__ == '__main__':
    solve()