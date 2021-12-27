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
    
    n = II()
    r = [(j,i+1) for i,j in enumerate(LI())]
    c = [(j,i+1) for i,j in enumerate(LI())]
    q = II()
    rc = LIR(q)
    r.sort(reverse=True)
    c.sort(reverse=True)
    rd = defaultdict(int)
    cd = defaultdict(int)
    for j,i in enumerate(r):
        rd[i[1]] = j
    for j,i in enumerate(c):
        cd[i[1]] = j
    for r, c in rc:
        r = rd[r]
        c = cd[c]
        if r >= c:
            if n - r  <= c:
                print(".", end="")
            else:
                print("#", end="")
        else:
            if n - c  <= r:
                print(".", end="")
            else:
                print("#", end="")
    print()
    

    return


#main
if __name__ == '__main__':
    solve()