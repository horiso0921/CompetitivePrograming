#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
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
    h,w,n = LI()
    sx, sy = LI()
    gx, gy = LI()
    xy = LIR(n)
    ox = defaultdict(list)
    oy = defaultdict(list)
    for x,y in xy:
        ox[x].append(y)
        oy[y].append(x)
    for k in list(ox.keys()):
        ox[k].sort()
    for k in list(oy.keys()):
        oy[k].sort()
    q = [(sx,sy)]
    dist = defaultdict(lambda: inf)
    dist[(sx, sy)] = 0
    for x,y in q:
        s = dist[(x,y)]
        uy = bisect_right(ox[x], y)
        if 0 <= uy < len(ox[x]):
            uy = ox[x][uy] - 1
            if gx == x and gy == uy:
                print(dist[(x,y)] + 1)
                return
            if dist[(x, uy)] > s + 1:
                dist[(x, uy)] = s + 1
                q.append((x, uy))
        uy = bisect_left(ox[x], y) - 1
        if 0 <= uy < len(ox[x]):
            uy = ox[x][uy] + 1
            if gx == x and gy == uy:
                print(dist[(x,y)] + 1)
                return
            if dist[(x, uy)] > s + 1:
                dist[(x, uy)] = s + 1
                q.append((x, uy))

        ux = bisect_right(oy[y], x)
        if 0 <= ux < len(oy[y]):
            ux = oy[y][ux] - 1
            if gx == ux and gy == y:
                print(dist[(x,y)] + 1)
                return
            if dist[(ux, y)] > s + 1:
                dist[(ux, y)] = s + 1
                q.append((ux, y))
        ux = bisect_left(oy[y], x) - 1
        if 0 <= ux < len(oy[y]):
            ux = oy[y][ux] + 1
            if gx == ux and gy == y:
                print(dist[(x,y)] + 1)
                return
            if dist[(ux, y)] > s + 1:
                dist[(ux, y)] = s + 1
                q.append((ux, y))
    print(-1)
    return



#main
if __name__ == '__main__':
    solve()