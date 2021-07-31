
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
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#solve
def D():
    h, w = LI()
    s = SR(h)
    new = [[] for i in range(h)]
    for y in range(h):
        for x in range(w):
            if s[y][x] == "#":
                f = True
                for my in range(-1, 2):
                    my += y
                    if 0 <= my < h:
                        for mx in range(-1, 2):
                            mx += x
                            if 0 <= mx < w:
                                if s[my][mx] == ".":
                                    f = False
                if f:
                    new[y].append("#")
                else:
                    new[y].append(".")
            else:
                new[y].append(".")
    for y in range(h):
        for x in range(w):
            if s[y][x] == "#":
                f = True
                for my in range(-1, 2):
                    my += y
                    if 0 <= my < h:
                        for mx in range(-1, 2):
                            mx += x
                            if 0 <= mx < w:
                                if new[my][mx] == "#":
                                    f = False
                if f:
                    print("impossible")
                    return
    print("possible")
    for ans in new:
        print("".join(ans))
    return

