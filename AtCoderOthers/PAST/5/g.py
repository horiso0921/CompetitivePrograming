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
    s = SR(h)
    ns = 0
    ans = []
    for y in range(h):
        for x in range(w):
            if s[y][x] == "#":
                ns += 1
    def dfs(y,x,check,n):
        if n == ns: 
            print(n)
            return True
        for my,mx in [(0,1),(1,0),(-1,0),(0,-1)]:
            my += y
            mx += x
            if 0 <= my < h and 0 <= mx < w and s[my][mx] == "#":
                if check[(my,mx)]: continue
                check[(my,mx)] = 1
                if dfs(my,mx, check,n+1):
                    print(my+1,mx+1)
                    return True       
                check[(my, mx)] = 0
        return False
    for y in range(h):
        for x in range(w):
            if s[y][x] == "#":
                c = defaultdict(int)
                c[(y,x)] = 1
                if dfs(y,x,c,1):
                    print(y+1,x+1)
                    return
    return


#main
if __name__ == '__main__':
    solve()