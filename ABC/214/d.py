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
    n = II()
    edg = []
    for _ in range(n-1):
        u,v,w = LI_()
        w += 1
        heappush(edg, ((w, u, v)))
    par = [i for i in range(n)]
    size = [1] * n
    def root(i):
        if par[i] == i:
            return i
        par[i] = root(par[i])
        return par[i]    
    def unite(x,y):
        x = root(x)
        y = root(y)
        if size[x] < size[y]: x,y = y,x
        size[x] += size[y]
        par[y] = x
    ans = 0
    while edg:
        w,u,v = heappop(edg)
        u = root(u)
        v = root(v)
        ans += size[u] * size[v] * w
        unite(u,v)
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()