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
def solve():
    def f(t):
        u = []
        d = []
        l = []
        r = []
        for x, y, c in xyc:
            u.append(y + t / c)
            d.append(y - t / c)
            l.append(x - t / c)
            r.append(x + t / c)
        return min(u) >= max(d) and min(r) >= max(l)

    n = II()
    xyc = LIR(n)
    ok = 200000000
    ng = 0
    while ok - ng > 1e-5:
        mid = (ok + ng) / 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    print(ok) 
    return


#main
if __name__ == '__main__':
    solve()
