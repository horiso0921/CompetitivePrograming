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
inf = float('INF')

#solve
def solve():
    n = II()
    for _ in range(n):
        nr, ng, nb = LI()
        r = LI()
        r.sort()
        g = LI()
        g.sort()
        b = LI()
        b.sort()
        ans = inf
        for ri in r:
            for gi in g:
                for bi in range(max(bisect_left(b, min(ri,gi)) - 1, 0), min(bisect_right(b, max(ri,gi)) + 1, nb)):
                    tmp = (ri - gi) ** 2 + (gi - b[bi]) ** 2 + (ri - b[bi]) ** 2
                    if tmp < ans:
                        ans = tmp
        print(ans)


    return


#main
if __name__ == '__main__':
    solve()
