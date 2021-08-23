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
    n, m, s = LI()
    uv = LIR_(m)
    edg = [[] for i in range(n)]
    for u, v in uv:
        edg[v].append(u)
        edg[u].append(v)
    c = [False] * n
    dp = [-1] * n
    q = deque([s - 1])
    c[s - 1] = True
    while q:
        p = q,
        score = dp[p]
        for e in edg[p]:
            if dp[e] == -1:
                if e < score: c[e] = True
                dp[e] = min(e, score)
                heappush(q, (-dp[e], e))
    for i in range(n):
        if c[i]:
            print(i + 1)
    return


#main
if __name__ == '__main__':
    solve()