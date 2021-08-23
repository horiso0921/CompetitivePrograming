
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
# 解説AC
# UnionFindまでは典型で
# 2つのparの組を持たせてかぶっているものがいくつあるのか
# という問題に帰着させることができなかった
def D():
    class UnionFind():

        def __init__(self, n):
            self.par = [i for i in range(n)]
            self.size = [1] * n
        
        def find(self, a):
            if a == self.par[a]:
                return a
            x = self.find(self.par[a])
            self.par[a] = x
            return x

        def unite(self, a, b):
            a = self.find(a)
            b = self.find(b)
            if a == b: return
            if a > b: a, b = b, a
            self.par[b] = a
            self.size[a] += self.size[b]

    n, k, l = LI()
    rail = UnionFind(n)
    road = UnionFind(n)

    for _ in range(k):
        p, q = LI_()
        rail.unite(p, q)
    for _ in range(l):
        r,s = LI_()
        road.unite(r, s)
    d = defaultdict(int)
    for i in range(n):
        d[(rail.find(i), road.find(i))] += 1
    for i in range(n):
        print(d[(rail.find(i), road.find(i))], end=" ")
    print()
    return

