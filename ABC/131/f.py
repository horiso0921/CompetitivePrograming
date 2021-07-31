
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
def F():
    n = II()
    xy = LIR(n)
    d = defaultdict(list)
    par = defaultdict(int)
    for _, y in xy:
        par[y] = y
    def root(x):
        if x == par[x]:
            return x
        par[x] = root(par[x])
        return par[x]
    
    def unite(x, y):
        x = root(x)
        y = root(y)
        if x == y:
            return False
        if x > y: x, y = y, x
        par[y] = x
        return True
    
    setx = set()
    for x, y in xy:
        d[x].append(y)
    for key, value in d.items():
        p = value[0]
        for v in value[1:]:
            unite(p, v)
    ans1 = defaultdict(int)
    ans2 = defaultdict(int)
    ans = 0
    for x, y in xy:
        root(y)
    # print(par)
    for _, value in d.items():
        ans1[par[value[0]]] += 1
    for _, value in par.items():
        ans2[value] += 1
    # print(ans1,ans2)
    for key, value in ans1.items():
        ans += ans2[key] * value
    print(ans - n)
    return

