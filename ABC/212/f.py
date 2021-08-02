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
inf = 1e10

#solve
def solve():
    n,m,Q = LI()
    q = []
    now = defaultdict(int)
    stop = defaultdict(int)
    for i in range(n):
        stop[i] = -1
    for _ in range(m):
        a,b,s,t = LI()
        heappush(q, (s+0.5,t+0.4,a-1,b-1,1))
    for i in range(Q):
        x,y,z = LI()
        heappush(q, (x,y-1,i,2))
        heappush(q, (z,i,3))
    par = [i for i in range(Q)]
    def root(i):
        if par[i] == i:
            return i
        par[i] = root(par[i])
        return par[i]
    size = [1] * Q
    def unite(a,b):
        a = root(a)
        b = root(b)
        if size[a] < size[b]:a,b = b,a
        if a == b: return
        par[b] = a
        size[a] += size[b]
        return
    ans = []
    while q:
        qe = heappop(q)
        if qe[-1] == 1:
            s,t,a,b,_ = qe
            if stop[a] != -1:
                p = stop[a]
                p = root(p)
                stop[a] = -1
                now[p] = (a+1,b+1)
                heappush(q, (t, b, p, 2))
        elif qe[-1] == 2:
            x,y,i,_ = qe
            if stop[y] != -1:
                unite(stop[y], i)
                i = root(i)
            now[i] = y+1
            stop[y] = i
        else:
            z,i,_ = qe
            xi = i
            i = root(i)
            ans.append((xi, now[i]))

    ans.sort()
    for _, a in ans:
        if type(a) == int:
            print(a)
        else:
            print(*a)
    return


#main
if __name__ == '__main__':
    solve()