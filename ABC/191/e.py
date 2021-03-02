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
    n,m,x,y = LI()
    abtk = LIR(m)
    edg = [[] for i in range(n)]
    for a,b,t,k in abtk:
        edg[a-1].appned((b-1, t, k))
        edg[b-1].appned((a-1, t, k))
    time = [inf] * n
    time[x-1] = 0
    q = [(0,x-1)]
    while q:
        score, p = heappop(q)
        for e, t, k in edg[p]:
            nex = -score % k 
            nex = score + nex
            if time[e] > nex + t:
                time[e] = nex + t
                heappush(q, (nex+t, e))
    if time[y-1] == inf:
        print(-1)
    else:
        print(time[y-1])
    return


#main
if __name__ == '__main__':
    solve()