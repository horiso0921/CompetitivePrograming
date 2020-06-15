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
def dij(start, edg, n):
    dist = [inf] * n
    dist[start] = 0
    q = [(0, start)]
    while q:
        score, p = heappop(q)
        for e in edg[p]:
            if dist[e] > score + 1:
                dist[e] = score + 1
                heappush(q, (score + 1, e))
    return dist

#solve
def solve():
    n, m = LI()
    uv = LIR_(m)
    edg = [[] for i in range(n)]
    for u, v in uv:
        edg[u].append(v)
        edg[v].append(u)
    s = II() - 1
    k = II()
    t = LI_()
    dp = [[inf] * (1 << k) for i in range(k)]
    d = defaultdict(int)
    for i, ti in enumerate(t):
        d[ti] = i
    full = defaultdict(list)
    for i in range(1 << k):
        full[sum(((i >> j) & 1 for j in range(k)))].append(i)
    dist = defaultdict(list)
    for i in range(k):
        dd = dij(t[i], edg, n)
        tmp = []
        for ti in t:
            tmp.append(dd[ti])
        dist[i] = tmp
    dd = dij(s, edg, n)
    for i in range(k):
        dp[i][1 << i] = dd[t[i]]
    for x in range(1, k):
        for mask in full[x]:
            for i in range(k):
                score = dp[i][mask]
                if score == inf: continue
                for j in range(k):
                    if mask == (mask | (1 << j)): continue
                    dp[j][mask | (1 << j)] = min(dp[j][mask | (1 << j)], dist[i][j] + score)
    print(min(map(lambda x: x[-1], dp)))
    return


#main
if __name__ == '__main__':
    solve()
