
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
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
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
def E():
    n, m = LI()
    xyz = LIR_(m)
    par = [i for i in range(n)]
    size = [1] * n
    def root(a):
        if par[a] == a:
            return a
        par[a] = root(par[a])
        return par[a]

    def union(a, b):
        a = root(a)
        b = root(b)
        if size[a] < size[b]: b, a = a, b
        if a == b:
            return
        par[b] = a
        size[b] += size[a]

    for x, y, _ in xyz:
        union(x, y)
    
    for i in range(n):
        root(i)
    print(len(set(par)))



    return

