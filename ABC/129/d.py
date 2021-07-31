
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
def D():
    h, w = LI()
    s = SR(h)
    dp = [[0] * w for _ in range(h)]
    for x in range(w):
        for y in range(h):
            if s[y][x] == ".":
                dp[y][x] += 1
    for y in range(h):
        x = 0
        q = 0
        while 0 <= x < w:
            if s[y][x] == ".":
                dp[y][x] += q
                q += 1
            else:
                q = 0
            x += 1
        x = w - 1
        q = 0
        while 0 <= x < w:
            if s[y][x] == ".":
                dp[y][x] += q
                q += 1
            else:
                q = 0
            x -= 1
    for x in range(w):
        y = 0
        q = 0
        while 0 <= y < h:
            if s[y][x] == ".":
                dp[y][x] += q
                q += 1
            else:
                q = 0
            y += 1
        y = h - 1
        q = 0
        while 0 <= y < h:
            if s[y][x] == ".":
                dp[y][x] += q
                q += 1
            else:
                q = 0
            y -= 1
    print(max(map(lambda x: max(x), dp)))
    return

