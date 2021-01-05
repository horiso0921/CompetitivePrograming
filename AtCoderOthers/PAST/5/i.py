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
def LFR(n): return [LF() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    n,m,k = LI()
    h = LI()
    c = LI_()
    edg = [[] for i in range(n)]
    for _ in range(m):
        a,b = LI_()
        if h[a] > h[b]:a,b = b,a
        edg[a].append(b)
    dist = [inf] * n
    q = []
    for ci in c:
        dist[ci] = 0
        heappush(q, (0, ci))
    while q:
        d, p = heappop(q)
        for e in edg[p]:
            if dist[e] > d + 1:
                heappush(q, (d+1, e))
                dist[e] = d+1
    for i in range(n):
        if dist[i] == inf:
            print(-1)
        else:
            print(dist[i])
    return


#main
if __name__ == '__main__':
    solve()