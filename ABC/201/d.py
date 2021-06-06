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
    h,w = LI()
    a = SR(h)
    dp = [[inf if j + i & 1 else -inf for j in range(w)] for i in range(h)]
    dp[-1][-1] = 0
    for hi in range(h - 1, -1, -1):
        for wi in range(w - 1, -1, -1):
            if hi + wi & 1 == 0:
                if wi != 0:
                    if a[hi][wi] == "-":
                        dp[hi][wi - 1] = min(dp[hi][wi] + 1, dp[hi][wi - 1])
                    else:
                        dp[hi][wi - 1] = min(dp[hi][wi] - 1, dp[hi][wi - 1])
                if hi != 0:
                    if a[hi][wi] == "-":
                        dp[hi - 1][wi] = min(dp[hi][wi] + 1, dp[hi - 1][wi])
                    else:
                        dp[hi - 1][wi] = min(dp[hi][wi] - 1, dp[hi - 1][wi])
            else:
                if wi != 0:
                    if a[hi][wi] == "-":
                        dp[hi][wi - 1] = max(dp[hi][wi] - 1, dp[hi][wi - 1])
                    else:
                        dp[hi][wi - 1] = max(dp[hi][wi] + 1, dp[hi][wi - 1])
                if hi != 0:
                    if a[hi][wi] == "-":
                        dp[hi - 1][wi] = max(dp[hi][wi] - 1, dp[hi - 1][wi])
                    else:
                        dp[hi - 1][wi] = max(dp[hi][wi] + 1, dp[hi - 1][wi])
    if dp[0][0] < 0:
        print("Aoki")
    elif dp[0][0] > 0:
        print("Takahashi")
    else:
        print("Draw")

    return


#main
if __name__ == '__main__':
    solve()