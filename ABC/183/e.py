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
inf = float("INF")

#solve
def solve():
    h,w = LI()
    s = SR(h)
    dp = [[0] * w for i in range(h)]
    dp1 = [[0] * w for i in range(h)]
    dp2 = [[0] * w for i in range(h)]
    dp3 = [[0] * w for i in range(h)]
    dp[0][0] = 1
    for y in range(h):
        dpy = dp[y]
        for x in range(w):
            if s[y][x] == ".":
                if y >= 1:
                    dpy[x] += dp1[y-1][x]
                if x >= 1:
                    dpy[x] += dp2[y][x-1]
                if y >= 1 and x >= 1:
                    dpy[x] += dp3[y-1][x-1]
                if y >= 1:
                    dp1[y][x] += dp1[y-1][x]
                if x >= 1:
                    dp2[y][x] += dp2[y][x-1]
                if y >= 1 and x >= 1:
                    dp3[y][x] += dp3[y-1][x-1]
                dpy[x] %= mod
                dp1[y][x] += dpy[x]
                dp2[y][x] += dpy[x]
                dp3[y][x] += dpy[x]
                dp1[y][x] %= mod
                dp2[y][x] %= mod
                dp3[y][x] %= mod
                
    print(dp[-1][-1])
                
    return


#main
if __name__ == '__main__':
    solve()
