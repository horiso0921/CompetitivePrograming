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
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR_(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI_()
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

#solve
def solve():
    def root(x):
        if x == par[x]:
            return x
        par[x] = root(par[x])
        return par[x]
    def unite(x, y):
        x = root(x)
        y = root(y)
        if x < y: x, y = y, x
        par[x] = y
        return
    for _ in range(II()):
        n, k = LI()
        par = [i for i in range(n)]
        for ans in range(n, 0, -1):
            

    return


#main
if __name__ == '__main__':
    solve()
