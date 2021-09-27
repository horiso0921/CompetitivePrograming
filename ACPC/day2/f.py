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
inf = 1e10

#solve
def solve():
    n,m,t = LI()
    u,s,j = LI_()
    edg = [[] for i in range(n)]
    for _ in range(m):
        a,b = LI_()
        edg[a].append(b)
        edg[b].append(a)
    def Dijkstra(num, start, vedge):
        """ vedge は DAG の 重みとして vedge[from] = (to, value)　としておくこと """
        """ DAGでない場合は vedge[from] と vedge[to] の両方を作ること """
        """ dist[i] は start から i までの最短距離 """

        dist = [inf for i in range(num)]
        dist[start] = 0
        q = [(dist[start], start)]
        while q:
            du, u = heappop(q)
            for e in vedge[u]:
                if dist[e] > du + 1:
                    dist[e] = du + 1
                    heappush(q, (dist[e], e))
        return dist
    distu = Dijkstra(n, u, edg)
    dists = Dijkstra(n, s, edg)
    distj = Dijkstra(n, j, edg)
    dist = [min(distu[e], dists[e], distj[e]) for e in range(n)]
    ok = 0
    ng = n + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2    
        ans = [inf] * n
        ans[0] = 0
        q = [(0, 0)]
        if dist[0] < mid: 
            ng = mid
            continue
        while q:
            du, p = heappop(q)
            for e in edg[p]:
                if dist[e] < mid: 
                    continue
                if ans[e] > du + 1:
                    ans[e] = du + 1
                    heappush(q, (du + 1, e))

        if ans[-1] > t:
            ng = mid
        else:
            ok = mid
    print(ok)
    return


#main
if __name__ == '__main__':
    solve()