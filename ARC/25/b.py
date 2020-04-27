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
    h,w = LI()
    c = LIR(h)
    for hi in range(h):
        for wi in range(w):
            c[hi][wi] *= - 1 if (hi + wi) & 1 else 1
    dp = [[0] * (w + 1) for i in range(h + 1)]
    for hi in range(h):
        for wi in range(w):
            dp[hi + 1][wi + 1] += c[hi][wi] + dp[hi + 1][wi]
    for hi in range(h):
        for wi in range(w):
            dp[hi + 1][wi + 1] += dp[hi][wi + 1]
    ans = 0
    for hl in range(h):
        for wl in range(w):
            for hr in range(hl + 1, h + 1):
                for wr in range(wl + 1, w + 1):
                    if dp[hr][wr] + dp[hl][wl] - dp[hr][wl] - dp[hl][wr] == 0:
                        ans = max(ans, (hr - hl) * (wr - wl))
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
