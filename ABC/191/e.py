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
inf = float("inf")

#solve
def solve():
    n,m = LI()
    edg = [[] for i in range(n)]
    def dijk(start):
        q = [(0, start)]
        dist = [inf] * 2000
        while q:
            score, point = heappop(q)
            if dist[point] < score: continue 
            for e, c in edg[point]:
                if score + c < dist[e]:
                    dist[e] = score + c
                    heappush(q, (score + c, e))
        return dist[start]
    for _ in range(m):
        a,b,c = LI_()
        c += 1
        edg[a].append((b,c))
    for i in range(n):
        ans = dijk(i)
        if ans == inf:
            print(-1)
        else:
            print(ans)
    return


#main
if __name__ == '__main__':
    solve()