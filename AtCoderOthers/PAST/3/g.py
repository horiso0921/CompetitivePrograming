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
    n, X, Y = LI()
    xy = defaultdict(int)
    for i in range(n):
        xy[tuple(LI())] = 1
    move = [(1, 1), (0, 1), (-1, 1), (1, 0), (-1, 0), (0, -1)]
    dist = defaultdict(lambda: inf)
    q = []
    dist[(0,0)] = 0
    q.append((0,(0, 0)))
    while q:
        s, x_y = heappop(q)
        x,y = x_y
        for mx, my in move:
            mx += x
            my += y
            if -210 <= mx < 210 and -210 <= my < 210:
                if xy[(mx, my)]:
                    continue
                if dist[(mx, my)] <= s + 1:
                    continue
                dist[(mx, my)] = s + 1
                heappush(q, (s + 1, (mx, my)))
    if dist[(X, Y)] == inf:
        print(-1)
    else:
        print(dist[(X, Y)])
    return


#main
if __name__ == '__main__':
    solve()
