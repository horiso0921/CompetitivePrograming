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

#solve
def solve():
    n = II()
    h = LI()
    dp = [inf] * n
    dp[0] = 0
    for i in range(1, n-1):
        dp[i] = min(dp[i], dp[i-1]+abs(h[i]-h[i-1]))
        dp[i+1] = min(dp[i+1], dp[i-1]+abs(h[i+1]-h[i-1]))
    dp[-1] = min(dp[-1], dp[-2]+abs(h[-1]-h[-2]))
    print(dp[-1])
    return


#main
if __name__ == '__main__':
    solve()