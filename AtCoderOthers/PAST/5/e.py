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
    move = [(0,1),(1,0),(-1,0),(0,-1)]
    h,w = LI()
    s = SR(h)
    t = SR(h)
    f = 0
    movlis = [(0,0)]
    for y in range(h):
        for x in range(w):
            if t[y][x] == "#":
                check = defaultdict(int)
                tmp = [(y,x)]
                yy = y
                xx = x
                check[(y,x)] = 1
                for y,x in tmp:
                    for my, mx in move:
                        my += y
                        mx += x
                        if check[(my,mx)]:
                            continue
                        if 0 <= my < h and 0 <= mx < w:
                            if t[my][mx] == "#":
                                tmp.append((my,mx))
                                check[(my,mx)] = 1
                                movlis.append((-yy+my, -xx+mx))
                                
                f = 1
            if f:
                break
        if f:
            break
    ans = 0
    
    for y in range(h):
        for x in range(w):
            for _ in range(4):
                t = 1
                for i in range(len(movlis)):
                    movlis[i] = [-movlis[i][1],movlis[i][0]]
                for my, mx in movlis:
                    my += y
                    mx += x
                    if 0 <= my < h and 0 <= mx < w:
                        if s[my][mx] == "#":
                            t = 0
                    else:
                        t = 0
                ans |= t
    print(["No", "Yes"][ans])


#main
if __name__ == '__main__':
    solve()