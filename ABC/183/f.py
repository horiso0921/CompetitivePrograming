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
inf = float("INF")

#solve
def solve():
    n,q = LI()
    c = LI()
    par = [i for i in range(n)]
    size = [1] * n
    dic = [defaultdict(int) for i in range(n)]
    for i in range(n):
        dic[i][c[i]] = 1
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
        par[y] = x
        size[x] += size[y]
        for key, val in dic[y].items():
            dic[x][key] += val
    for _ in range(q):
        q = LS()
        if q[0] == "1":
            a,b = map(int, q[1:])
            unite(a-1,b-1)
        else:
            x,y = map(int, q[1:])
            x = root(x-1)
            print(dic[x][y])
    return


#main
if __name__ == '__main__':
    solve()
