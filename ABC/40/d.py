
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
def D():
    def find(a):
        if a == par[a]:
            return a
        par[a] = find(par[a])
        return par[a]

    def unite(a, b):
        a = find(a)
        b = find(b)
        if rank[a] < rank[b]: a, b = b, a
        if a == b: return
        par[b] = a
        rank[a] += rank[b]
    
    n, m = LI()
    rank = [1] * n
    par = [i for i in range(n)]
    lis = []
    for _ in range(m):
        a, b, y = LI_()
        lis.append((y, a, b))
    q = II()
    for i in range(q):
        v, w = LI_()
        lis.append((w, i + n, v))
    lis.sort(reverse = True)
    ans = [None] * q
    for l in lis:
        if l[1] >= n:
            ans[l[1] - n] = rank[find(l[2])]
        else:
            unite(l[1], l[2])
    for a in ans:
        print(a)
    return


