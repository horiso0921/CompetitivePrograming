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
    q = II()
    tx = LIR(q)
    ans = [-1] * 1048576
    n = 1048576
    par = [i for i in range(n)]
    def root(x):
        if par[x] == x:
            return x
        par[x] = root(par[x])
        return par[x]
    def unite(x,y):
        x = root(x)
        y = root(y)
        par[x] = y
        return
    for t,x in tx:
        xt = x % n
        if t == 1:
            tt = root(xt)
            ans[tt] = x
            if tt == n - 1:
                unite(tt, 0)
            else:
                unite(tt, tt+1)
        else:
            print(ans[xt])
    

    
    return



#main
if __name__ == '__main__':
    solve()