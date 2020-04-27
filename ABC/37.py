#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    a, b, c = LI()
    a, b = max(a, b), min(a, b)
    ans = c // b
    for i in range(c // a):
        x = c - a * i
        ans = max(ans, i + x // b)
    print(ans)
    return

#B
def B():
    n, q = LI()
    ans = [0] * n
    for _ in range(q):
        l, r, t = LI()
        ans[l - 1:r] = [t] * (r - l + 1)
    for i in range(n):
        print(ans[i])
    return

#C
def C():
    n, k = LI()
    a = LI()
    ans = 0
    for i in range(n):
        ans += a[i] * min(i + 1, k, n - k + 1, n - i)
    print(ans)
    return

#D
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

#Solve
if __name__ == '__main__':
    D()
