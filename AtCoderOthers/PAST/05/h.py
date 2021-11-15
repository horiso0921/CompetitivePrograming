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
    h,w = LI()
    r,c = LI()
    s = SR(h)
    ans = [["x"]*w for i in range(h)]
    for y in range(h):
        for x in range(w):
            if s[y][x] == "#":
                ans[y][x] = "#"
    move = [(0,1,"<"),(1,0,"^"),(-1,0,"v"),(0,-1,">")]
    m = [(r-1,c-1)]
    ans[r-1][c-1] = "o"
    for y,x in m:
        for my, mx, p in move:
            my += y
            mx += x
            if 0 <= my < h and 0 <= mx < w:
                if s[my][mx] == p or s[my][mx] == ".":
                    if ans[my][mx] == "x":
                        ans[my][mx] = "o"
                        m.append((my,mx))
    for a in ans:
        print("".join(a))
        
    return


#main
if __name__ == '__main__':
    solve()