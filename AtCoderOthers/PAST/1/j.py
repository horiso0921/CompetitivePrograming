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
mxy = [(0, 1), (1, 0), (-1, 0), (0, -1)]
#solve
def solve():
    h, w = LI()
    a = LIR(h)
    dp1 = [[inf] * w for i in range(h)]
    dp2 = [[inf] * w for i in range(h)]
    dp3 = [[inf] * w for i in range(h)]
    def f(dp,sx,sy):
        q = [(0, (sx, sy))]
        while q:
            s, p = heappop(q)
            x, y = p
            for mx, my in mxy:
                mx += x
                my += y
                if 0 <= mx < w and 0 <= my < h:
                    if dp[my][mx] <= s + a[my][mx]: continue
                    dp[my][mx] = s + a[my][mx]
                    heappush(q, (s + a[my][mx], (mx, my)))
        return dp
    dp1[-1][0] = 0
    dp2[-1][-1] = 0
    dp3[0][-1] = 0
    dp1 = f(dp1, 0, h - 1)
    dp2 = f(dp2, w - 1, h - 1)
    dp3 = f(dp3, w - 1, 0)
    ans = inf
    for i in range(w):
        for j in range(h):
            ans = min(ans, dp1[j][i] + dp2[j][i] + dp3[j][i] - a[j][i] * 2)
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
