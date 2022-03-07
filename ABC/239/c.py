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
    x1,y1,x2,y2 = LI()
    mxy = [(x,y) for x in range(-2, 3) for y in range(-2, 3) if abs(x) + abs(y) == 3]
    
    cand = defaultdict(int)
    for mx,my in mxy:
        mx += x1
        my += y1
        cand[(mx, my)] = 1
    for mx,my in mxy:
        mx += x2
        my += y2
        if cand[(mx,my)]:
            print("Yes")
            return
    print("No")
    return
        
    return


#main
if __name__ == '__main__':
    solve()