#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
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
    def dij(g, s, n):
        dist = [inf] * n
        dist[s] = 0
        q = [(0, s)]
        while q:
            score, p = heappop(q)
            if dist[p] < score: continue
            for e, c in g[p]:
                if score + c < dist[e]:
                    dist[e] = score + c
                    heappush(q, (score + c, e))
        return dist
    n,m = LI()
    edg = [[] for i in range(n+1)]
    for _ in range(m):
        l,r = LI()
        l -= 1
        edg[l].append((r,0))
        edg[r].append((l,0))
    for i in range(n):
        edg[i].append((i+1, 1))
        edg[i+1].append((i, 1))
    cost = dij(edg, 0, n+1)
    for i in range(n):
        if cost[i] < cost[i+1]:print("0", end="")
        else:print("1", end="")
    print()
    return



#main
if __name__ == '__main__':
    solve()