#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def IR(n):
    return [I() for _ in range(n)]
def LIR(n):
    return [LI() for _ in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    def check(x,y,sx,sy,tx,ty,r):
        if (x-sx)**2+(y-sy)**2 <= r**2:
            return 1
        if (x-tx)**2+(y-ty)**2 <= r**2:
            return 1
        if sx == tx:
            mx = sx
            my = y
        elif sy == ty:
            mx = x
            my = sy
        else:
            a1 = tx-sx
            a2 = ty-sy
            b1 = x-sx
            b2 = y-sy
            q = a1**2+a2**2
            mx = sx*q+(a2*b2+a1*b1)*a1
            my = sy*q+(a2*b2+a1*b1)*a2
            x *= q
            y *= q
            sx *= q
            sy *= q
            tx *= q
            ty *= q
            r *= q
        a,b = (mx-sx,my-sy)
        c,d = (tx-sx,ty-sy)
        if c < 0:
            if a > 0 or a < c:
                return 0
        else:
            if a < 0 or a > c:
                return 0
        if d < 0:
            if b > 0 or b < d:
                return 0
        else:
            if b < 0 or b > d:
                return 0
        if (x-mx)**2+(y-my)**2 <= r**2:
            return 1
        return 0
    r = I()
    sx,sy = LI()
    tx,ty = LI()
    q = I()
    for _ in range(q):
        x,y = LI()
        if check(x,y,sx,sy,tx,ty,r):
            print("Yes")
        else:
            print("No")
    return

#Solve
if __name__ == "__main__":
    solve()

