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
    n, m = LI()
    ab = LIR(m)
    par = [i for i in range(n)]
    size = [1] * n
    def root(x):
        if par[x] == x:
            return x
        par[x] = root(par[x])
        return par[x]
    def unite(a, b):
        a = root(a)
        b = root(b)
        if a == b:
            return
        if size[a] < size[b]: a, b = b, a
        par[b] = a
        size[a] += size[b]
    for a, b in ab:
        a -= 1
        b -= 1
        unite(a, b)
    
    print(max(size))
    return


#main
if __name__ == '__main__':
    solve()