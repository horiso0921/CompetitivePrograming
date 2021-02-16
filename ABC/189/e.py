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
def LFR(n): return [LF() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    n = II()
    xy = LIR(n)
    m = II()
    op = LIR(m)
    q = II()
    ab = LIR(q)
    opab = [(i, *op[i]) for i in range(m)] + [(ab[i][0]-0.1, i, ab[i][1]) for i in range(q)]
    opab.sort()
    xp = 0
    xpc = 0
    yp = 0
    ypc = 0
    rotate = 0
    ans = [None] * q
    for i, *ab in opab:
        if i == int(i):
            i = int(ab[0])
            if i == 1:
                rotate -= 1
                xp,yp = yp, -xp
                xpc,ypc = ypc,xpc
            elif i == 2:
                rotate += 1
                xp,yp = -yp, xp
                xpc,ypc = ypc,xpc
            elif i == 3:
                xp = -xp + 2 * ab[1]
                xpc += 1
            else:
                yp = -yp + 2 * ab[1]
                ypc += 1
        else:
            i = ab[1] - 1
            a,b = xy[i]
            for i in range(rotate % 4):
                a,b = -b,a
            ans[ab[0]] = ([1,-1][xpc&1]*a+xp, [1,-1][ypc&1]*b+yp)
    for a in ans:
        print(*a)
    return


#main
if __name__ == '__main__':
    solve()