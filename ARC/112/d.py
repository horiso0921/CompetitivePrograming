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
inf = 1e10

#solve
def solve():
    h,w = LI()
    s = SR(h)
    par = defaultdict(lambda: (0,0))
    for i in range(h):
        par[(i,-1)] = (i,-1)
    for i in range(w):
        par[(-1,i)] = (-1,i)
    def root(x):
        if par[x] == x:
            return x
        par[x] = root(par[x])
        return par[x]
    def unite(x,y):
        x = root(x)
        y = root(y)
        if x > y:x,y=y,x
        par[y] = x
        return 
    unite((0,-1),(-1,0))
    unite((0,-1),(-1,w-1))
    unite((-1,w-1),(h-1,-1))
    unite((h-1,-1),(-1,0))
    for y in range(h):
        for x in range(w):
            if s[y][x] == "#":
                unite((y,-1),(-1,x))
    seta = set()
    setb = set()
    for y in range(h):
        seta.add(root((y,-1)))
    for x in range(w):
        setb.add(root((-1,x)))
    print(min(len(seta), len(setb))-1)
        
        
    return


#main
if __name__ == '__main__':
    solve()
    
    