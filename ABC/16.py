#!usr/bin/env python3
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
    m, d = LI()
    if not m % d:
        print("YES")
    else:
        print("NO") 
    return

#B
def B():
    a, b, c = LI()
    if c - a == b:
        if c + b == a:
            print("?")
        else:
            print("+")
    elif c + b == a:
        print("-")
    else:
        print("!")
    return

#C
def C():
    n,m = LI()
    lis = [[] for i in range(n)]
    for _ in range(m):
        a, b = LI_()
        lis[a].append(b)
        lis[b].append(a)
    for num, li in enumerate(lis):
        ans = []
        for l in li:
            for ll in lis[l]:
                if ll != num and not ll in li:
                    ans.append(ll)
        
        print(len(set(ans)))


    return

#D
def D():
    ax, ay, bx, by = LI()
    v1 = [bx - ax, by - ay]
    n = II()
    ans = 0
    v = LIR(n)
    for i in range(n):
        a, b = v[i]
        c, d = v[i - 1]
        v2 = [a - ax, b - ay]
        v3 = [c - ax, d - ay]
        v4 = [c - a, d - b]
        v5 = [ax - a, ay - b]
        v6 = [bx - a, by - b]
        s1 = (v1[0] * v2[1] - v2[0] * v1[1])
        s2 = (v1[0] * v3[1] - v3[0] * v1[1])
        s3 = (v4[0] * v5[1] - v5[0] * v4[1])
        s4 = (v4[0] * v6[1] - v6[0] * v4[1])
        if s1 * s2 < 0 and s3 * s4 < 0:
            ans += 1
    def wrong_ans():
        if ax - bx == 0:
            tilt = inf
        else:
            tilt = (ay - by) / (ax - bx)
        for i in range(n):
            a, b = v[i]
            c, d = v[i - 1]
            if c - a == 0:
                if tilt == 0:
                    if min(ax, bx) < c < max(ax, bx):
                        ans += 1
                elif tilt == inf:
                    continue
                else:
                    y = tilt * a - tilt * ax + ay
                    if min(b, d) < y < max(b, d):
                        ans += 1
            elif b - d == 0:
                if tilt == 0:
                    continue
                elif tilt == inf:
                    if min(ay, by) < b < max(ay, by):
                        ans += 1
                    else:
                        x = (b - ay + tilt * ax) / tilt
                    if min(a, c) < x < max(a, c):
                        ans += 1
            else:
                tilt_ = (d - b) / (c - a)
                if tilt == 0:
                    x = (ay - b + tilt_ * a) / tilt_
                    if min(ax, bx) < x < max(ax, bx):
                        ans += 1
                elif tilt == inf:
                    y = tilt_ * ax - tilt_ * a + b
                    if min(ay, by) < y < max(ay, by):
                        ans += 1
                else:
                    if tilt_ == tilt:
                        continue
                    x = (tilt_ * a - tilt * ax + ay - b) / (tilt_ - tilt)
                    if min(ax, bx) < x < max(ax, bx):
                        ans += 1
    print(ans//2+1)



    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    D()
