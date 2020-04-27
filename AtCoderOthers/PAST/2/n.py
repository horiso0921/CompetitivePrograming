#!/usr/bin/env python4
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
    dx = defaultdict(lambda :inf)
    dy = defaultdict(lambda: inf)
    di = defaultdict(tuple)
    lx = [-inf,inf]
    ly = [-inf,inf]
    n, q = LI()
    for i in range(n):
        x, y, d, c = LI()
        di[i] = (x, y, d, c)
        lx.append(x - 1)
        lx.append(x)
        lx.append(x + d)
        lx.append(x + d + 1)
        ly.append(y - 1)
        ly.append(y)
        ly.append(y + d)
        ly.append(y + d + 1)
    lx.sort()
    ly.sort()
    dp = [[0] * (4 * n + 2) for _ in range(4 * n + 2)]
    for i in range(4 * n + 2):
        dx[lx[i]] = min(i,dx[lx[i]])
        dy[ly[i]] = min(i,dy[ly[i]])
    for i in range(n):
        x, y, d, c = di[i]
        dp[dx[x]][dy[y]] += c
        dp[dx[x + d + 1]][dy[y + d + 1]] += c
        dp[dx[x]][dy[y + d + 1]] -= c
        dp[dx[x + d + 1]][dy[y]] -= c
    for i in range(4 * n + 2):
        for j in range(4 * n + 1):
            dp[i][j + 1] += dp[i][j]
    for i in range(4 * n + 1):
        for j in range(4 * n + 2):  
            dp[i + 1][j] += dp[i][j]
    for _ in range(q):
        a, b = LI()
        x = bisect_left(lx, a)
        y = bisect_left(ly, b)
        print(dp[x][y])
    return


#main
if __name__ == '__main__':
    solve()
