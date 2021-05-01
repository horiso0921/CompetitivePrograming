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
inf = 1e30

#solve
def solve():
    R,C = LI()
    a = LIR(R)
    b = LIR(R-1)
    q = [(0, (0,0))]
    dist = [[inf] * C for i in range(R)]
    dist[0][0] = 0
    while q:
        s, p = heappop(q)
        r,c = p
        if c < C - 1:
            if dist[r][c+1] > s + a[r][c]:
                dist[r][c+1] = s + a[r][c]
                heappush(q, (s + a[r][c], (r, c + 1)))
        if c > 0:
            if dist[r][c-1] > s + a[r][c-1]:
                dist[r][c-1] = s + a[r][c-1]
                heappush(q, (s + a[r][c-1], (r, c - 1)))
        if r < R - 1:
            if dist[r+1][c] > s + b[r][c]:
                dist[r+1][c] = s + b[r][c]
                heappush(q, (s + b[r][c], (r+1, c)))
        for i in range(1, r+1):
            if dist[r-i][c] > s + i+1:
                dist[r-i][c] = s + i+1
                heappush(q, (s + i+1, (r-i, c)))
        # print(dist,p)
    print(dist[-1][-1])
    return


#main
if __name__ == '__main__':
    solve()