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
def IR(n):
    res = [None] * n
    for i in range(n):
        res[i] = II()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI()
    return res
def FR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIF(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def SR(n):
    res = [None] * n
    for i in range(n):
        res[i] = S()
    return res
def LSR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LS()
    return res
mod = 1000000007
inf = float('INF')

class UnionFind():
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.size = [1] * n

    def root(self,x):
        if x == self.par[x]:
            return x
        r = self.root(self.par[x])
        self.par[x] = r
        return r

    def unit(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y: return False
        if self.size[x] < self.size[y]: x, y = y, x
        self.size[x] += self.size[y]
        self.par[y] = x
        return True
    
    def getsize(self, x):
        x = self.root(x)
        return self.size[x]


#solve
def solve():
    h, w = LI()
    s = SR(h)
    rowunion = [UnionFind(w) for i in range(h)]
    colunion = [UnionFind(h) for i in range(w)]
    dot = 0
    for y in range(h):
        sy = s[y]
        for x in range(w):
            if sy[x] == ".":
                dot += 1
    for y in range(h):
        sy = s[y]
        rowy = rowunion[y]
        for x in range(w-1):
            if sy[x] == ".":
                if sy[x + 1] == ".":
                    rowy.unit(x, x + 1)
    for x in range(w):
        colx = colunion[x]
        for y in range(h-1):
            if s[y][x] == ".":
                if s[y+1][x] == ".":
                    colx.unit(y, y + 1)
    pow2 = [1] * (dot + 1)
    for i in range(dot):
        pow2[i+1] = (pow2[i] * 2) % mod
    l = pow2[dot]
    ans = l * dot
    ans %= mod
    d = [[0] * w for i in range(h)]
    for y in range(h):
        ry = rowunion[y]
        for x in range(w):
            d[y][x] = ry.getsize(x)
    for x in range(w):
        cx = colunion[x]
        for y in range(h):
            d[y][x] += cx.getsize(y)
    for y in range(h):
        sy = s[y]
        for x in range(w):
            if sy[x] == "#": continue
            tmp = d[y][x] - 1
            ans -= pow2[dot - tmp]
            ans %= mod
    print(ans)
    
    return


#main
if __name__ == '__main__':
    solve()
