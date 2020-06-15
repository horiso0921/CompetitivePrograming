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
    n, m = LI()
    xyc = LIR(n)
    XYC = LIR(m)
    mainlis = []
    f = lambda x1, y1, x2, y2: sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    for i in range(n):
        for j in range(i + 1, n):
            xi, yi, ci = xyc[i]
            Xi, Yi, Ci = xyc[j]
            dist = f(xi, yi, Xi, Yi)
            if ci != Ci: dist *= 10
            heappush(mainlis, (dist, (i, j)))
    def root(a):
        if a == par[a]:
            return a
        par[a] = root(par[a])
        return par[a]
    def unite(a, b):
        a = root(a)
        b = root(b)
        if a > b: b, a = a, b
        par[b] = a
        return
    aaa = inf
    for mask in range(1 << m):
        tmp = mainlis[::1]
        for i in range(m):
            if mask & (1 << i):
                for j in range(n):
                    xi, yi, ci = xyc[j]
                    Xi, Yi, Ci = XYC[i]
                    dist = f(xi, yi, Xi, Yi)
                    if ci != Ci: dist *= 10
                    heappush(tmp, (dist, (j, i + n)))
                for j in range(m):
                    if mask & (1 << j):
                        xi, yi, ci = XYC[j]
                        Xi, Yi, Ci = XYC[i]
                        dist = f(xi, yi, Xi, Yi)
                        if ci != Ci: dist *= 10
                        heappush(tmp, (dist, (j + n, i + n)))
        par = [i for i in range(n + m)]
        ans = 0
        while tmp:
            s, ij = heappop(tmp)
            i, j = ij
            if root(i) == root(j): continue
            unite(i, j)
            ans += s
        aaa = min(aaa, ans)
    print(aaa)

    return


#main
if __name__ == '__main__':
    solve()
