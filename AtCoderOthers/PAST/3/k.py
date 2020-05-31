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

#solve
def solve():
    n, q = LI()
    ftx = LIR_(q)
    cont_head = [i for i in range(n)]
    in_edg = [i + n for i in range(n)]
    out_edg = [None for j in range(2 * n)]
    for i in range(n):
        out_edg[n + i] = i
    for f, t, x in ftx:
        out_edg[in_edg[x]] = None
        tt = cont_head[t]
        ii = in_edg[x]
        in_edg[x] = tt
        cont_head[t] = cont_head[f]
        cont_head[f] = ii
        out_edg[tt] = x
    ans = [None] * n
    for i in range(n):
        j = n + i
        while out_edg[j] != None:
            j = out_edg[j]
            ans[j] = i + 1
        if j < n:
            ans[j] = i + 1
    for ai in ans:
        print(ai)


    return


#main
if __name__ == '__main__':
    solve()
