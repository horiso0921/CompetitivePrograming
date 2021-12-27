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
    h,w,k = LI()
    x1,y1,x2,y2 = LI()
    dp = [0, 0, 0, 1]
    for _ in range(k):
        ndp = [0, 0, 0, 0]
        ndp[0] = dp[0] * (w + h - 4) + dp[1] + dp[2]
        ndp[1] = dp[1] * (w - 2) + dp[0] * (h - 1) + dp[3]
        ndp[2] = dp[2] * (h - 2) + dp[0] * (w - 1) + dp[3]
        ndp[3] = dp[1] * (w - 1) + dp[2] * (h - 1)
        dp = [d % mod for d in ndp]
        # print(dp)
    if x1 == x2:
        if y1 == y2:
            print(dp[3])
        else:
            print(dp[1])
    else:
        if y1 == y2:
            print(dp[2])
        else:
            print(dp[0])
    return


#main
if __name__ == '__main__':
    solve()