#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import re
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
    d = LI()
    if sum(d) != 2 * n - 2: 
        print(-1)
        return
    par = [i for i in range(n)]
    edg = [[] for _ in range(n)]
    for i in range(n):
        for _ in range(d[i]):
            edg[i].append(i)
    def root(x):
        if par[x] == x:
            return x
        par[x] = root(par[x])
        return par[x]
    def unite(x,y):
        x = root(x)
        y = root(y)
        if len(edg[x]) > len(edg[y]): 
            x,y = y,x
        p1 = edg[y].pop()
        p2 = edg[x].pop()
        edg[y].extend(edg[x])
        edg[x] = []
        par[x] = y
        return p1+1, p2+1, y

    f = 0
    for _ in range(m):
        a,b = LI_()
        d[a]-=1
        d[b]-=1
        if d[a] < 0:
            f = -1
        if d[b] < 0:
            f = -1
        if root(a) == root(b):
            f = -1
        if f != -1:
            unite(a,b)
    
    if f == -1:
        print(-1)
        return
    
    que = []
    edg = [[] for _ in range(n)]
    for pi in range(n):
        if d[pi]:
            rootp = root(pi)
            edg[rootp].extend([pi] * d[pi])
    for pi in range(n):
        if pi == root(pi):
            if edg[pi]:
                heappush(que, (-len(edg[pi]), pi))

    ans = []
    while len(que) >= 2:
        s1,p1 = heappop(que)
        s2,p2 = heappop(que)
        x, y, s = unite(p1, p2)
        ans.append((min(x,y), max(x,y)))
        if s1 + s2 + 2 < 0:
            heappush(que, (s1 + s2 + 2, s))
    if len(ans) != n - m - 1:
        print(-1)
        return
    for a in ans:
        print(a[0], a[1])
    return
    
        


#main
if __name__ == '__main__':
    solve()