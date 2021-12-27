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
    n,m = LI()
    size = [0] * n
    par = [i for i in range(n)]
    def root(x):
        if par[x] == x:
            return par[x]
        par[x] = root(par[x])
        return par[x]
    
    def unite(a,b):
        a = root(a)
        b = root(b)
        if size[a] > size[b]: a,b = b,a
        if a == b: return False
        par[a] = b
        size[b] += size[a]
        return True
    
    ab = LIR_(m)
    ans = [0] * n
    edg = [[] for i in range(n)]
    for a,b in ab:
        if a > b:a,b = b,a
        edg[a].append(b)

    x = 0
    
    for i in range(n-1, -1, -1):
        ans[i] = x
        x += 1
        for e in edg[i]:
            x -= unite(i,e)
    for ai in ans:
        print(ai)
    return


#main
if __name__ == '__main__':
    solve()