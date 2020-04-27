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
    n, k = LI()
    a = LI()
    dp = [0] * n
    for i in range(1, n - 1):
        dp[i + 1] = a[i + 1] < a[i] and a[i] > a[i - 1]
    dp = list(itertools.accumulate(dp))
    ans = [1, 1]
    print(dp)
    for i in range(n - k + 1):
        if ans[0] < dp[i + k - 1] - dp[i] + 1:
            ans = [dp[i + k - 1] - dp[i] + 1, i + 1]
    print(ans[0], ans[1])
    return


#main
if __name__ == '__main__':
    for _ in range(II()):
        solve()
