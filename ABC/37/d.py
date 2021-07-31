
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
    def dfs(y, x):
        if dp[y][x]:
            return dp[y][x]
        tmp = 1
        now = a[y][x]
        for mx, my in move:
            mx += x
            my += y
            if 0 <= mx < w and 0 <= my < h and a[my][mx] > now:
                tmp += dfs(my, mx) % mod
        dp[y][x] = tmp
        return tmp % mod
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    h, w = LI()
    a = LIR(h)
    dp = [[0] * w for i in range(h)]
    for y in range(h):
        for x in range(w):
            dfs(y,x)
    ans = 0
    for i in dp:
        ans += sum(i) % mod
    print(ans % mod)
    return

