#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import re
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
    s = S()
    sa = 0
    for si in s:
        if si == "a":
            sa += 1
        else:
            break
    ea = 0
    for si in s[::-1]:
        if si == "a":
            ea += 1
        else:
            break
    if sa > ea:
        print("No")
        return
    l = sa
    r = len(s) - 1 - ea
    while l <= r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            print("No")
            return
    print("Yes")
    return


#main
if __name__ == '__main__':
    solve()