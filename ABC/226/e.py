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
mod = 998244353
inf = 1e10

#solve
def solve():
    n,m = LI()
    if n != m:
        print(0)
        return
    edg = [[] for i in range(n)]
    par = [i for i in range(n)]
    size = [1] * n
    def root(x):
        if par[x] == x:
            return x
        par[x] = root(par[x])
        return par[x]
    def unite(x,y):
        x = root(x)
        y = root(y)
        if x == y: return
        if size[x] < size[y]: x,y = y,x
        size[x] += size[y]
        par[y] = x
    for _ in range(m):
        u,v = LI_()
        edg[u].append(v)
        edg[v].append(u)
        unite(u,v)
    r = set()
    for i in range(n):
        ri = root(i)
        r.add(ri)
    for rx in r:
        size[rx] *= 2
    for i in range(n):
        ri = root(i)
        size[ri] -= len(edg[i])
    ans = 1
    for rx in r:
        if size[rx] != 0:
            print(0)
            return
        ans *= 2
        ans %= mod
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()