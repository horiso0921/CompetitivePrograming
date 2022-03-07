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
    n,Q = LI()
    x = LI()
    edg = [[] for i in range(n)]
    for _ in range(n-1):
        a,b = LI_()
        edg[a].append(b)
        edg[b].append(a)
    big = [[-x[i]] for i in range(n)]
    q = [0]
    c = [0] * n
    c[0] = 1
    for qi in q:
        for e in edg[qi]:
            if c[e]: continue
            c[e] = 1
            q.append(e)

    c = [0] * n
    for qi in reversed(q):
        c[qi] = 1
        buff = []
        for _ in range(20):
            if big[qi]:
                x = heappop(big[qi])
                buff.append(x)
        for b in buff:
            heappush(big[qi], b)

        for e in edg[qi]:

            if c[e]: continue
            for b in buff:
                heappush(big[e], b)
    for _ in range(Q):
        v,k = LI()
        v -= 1
        
        buff = []
        for _ in range(k):
            if big[v]:
                x = heappop(big[v])
                buff.append(x)
        print(-buff[-1])
        
        for b in buff:
            heappush(big[v], b)
    return


#main
if __name__ == '__main__':
    solve()