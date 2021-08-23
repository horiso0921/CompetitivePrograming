#!/usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys
import random
import itertools
import math
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
    h, w = LI()
    c = SR(h)
    for i in range(w):
        for j in range(h):
            if c[j][i] == "s":
                s = (j, i)
            if c[j][i] == "g":
                g = (j, i)
    q = deque()
    q.append(s)
    dp = [[3] * w for _ in range(h)]
    dp[s[0]][s[1]] = 0
    m = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while q:
        y, x = q.popleft()
        t = dp[y][x]
        for mx, my in m:
            mx += x
            my += y
            if 0 <= mx < w and 0 <= my < h:
                if c[my][mx] == "." or c[my][mx] == "g":
                    if dp[my][mx] > t:
                        dp[my][mx] = t
                        q.appendleft((my, mx))
                elif c[my][mx] == "#":
                    if t == 2:
                        continue
                    if dp[my][mx] > t + 1:
                        dp[my][mx] = t + 1
                        q.append((my, mx))
    print("YES" if dp[g[0]][g[1]] <= 2 else "NO")

    return


#main
if __name__ == '__main__':
    solve()
