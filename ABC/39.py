#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    a, b, c = LI()
    print(a*b*2+b*c*2+a*c*2)
    return

#B
def B():
    x = II()
    s = math.sqrt
    print(int(s(s(x))))
    return

#C
def C():
    lis = "WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW"
    ans = ["Do",None,"Re",None,"Mi","Fa",None,"So",None,"La",None,"Si"]
    s = input()
    s = s[:12]
    for i in range(12):
        if lis[i:i + 12] == s:
            print(ans[i])
            return
    return

#D
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

#Solve
if __name__ == '__main__':
    D()
