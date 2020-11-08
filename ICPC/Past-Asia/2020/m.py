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
def IR(n):
    res = [None] * n
    for i in range(n):
        res[i] = II()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI()
    return res
def FR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIF(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def SR(n):
    res = [None] * n
    for i in range(n):
        res[i] = S()
    return res
def LSR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LS()
    return res
mod = 1000000007
inf = float('INF')


"""
Calculate the intersections of 2 circles, R1(x1,y1,r1) and R2(x2,y2,r2) : O(1)
ref : https://shogo82148.github.io/homepage/memo/geometry/circle-cross.html"
"""


def D2(x1,y1,x2,y2):
    return (x1-x2)**2+(y1-y2)**2


def check(R1,R2):
    x1,y1,r1 = R1
    x2,y2,r2 = R2
    d2 = D2(x1,y1,x2,y2)
    if (r1-r2)**2 <= d2 <= (r1+r2)**2:
        return 1
    else:
        return 0


def intersection(R1,R2):
    if not check(R1,R2):
        return []
    else:
        x1,y1,r1 = R1
        x2,y2,r2 = R2
        x2 -= x1
        y2 -= y1
        r = x2**2+y2**2
        a = (r+r1**2-r2**2)/2
        d = (r*r1**2-a**2)**0.5
        X,Y = a*x2/r, a*y2/r
        k = d/r
        X1,Y1 = X+y2*k+x1, Y-x2*k+y1
        X2,Y2 = X-y2*k+x1, Y+x2*k+y1
        return [(X1, Y1), (X2, Y2)]

"""
Calculate the intersections of 2 lines, l1(xs1,ys1,xt1,yt1) and l1(xs2,ys2,xt2,yt2) : O(1)
"""

def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]

def line_intersection(l1, l2):
    (xs1,ys1),(xt1,yt1) = l1
    (xs2,ys2),(xt2,yt2) = l2
    s1t1 = (xt1-xs1, yt1-ys1)
    s1s2 = (xs2-xs1, ys2-ys1)
    s1t2 = (xt2-xs1, yt2-ys1)
    if cross(s1t1, s1s2)*cross(s1t1, s1t2) >= 0:
        return None
    
    s2t2 = (xt2-xs2, yt2-ys2)
    s2s1 = (xs1-xs2, ys1-ys2)
    s2t1 = (xt1-xs2, yt1-ys2)
    
    crs = cross(s2t2, s2s1)
    crt = cross(s2t2, s2t1)
    if crs*crt >= 0:
        return None
    
    rate = abs(crs)/(abs(crs)+abs(crt))
    x,y = xs1+rate*s1t1[0], ys1+rate*s1t1[1]
    return x,y

#solve
def solve(n):
    xyr = LIR(n)
    p = [None] * (2 * n)
    gate = [None] * n
    for i in range(n - 1):
        gate[i] = intersection(xyr[i], xyr[i + 1])
        tmp = gate[i]
        p[2 * i] = tmp[0]
        p[2 * i + 1] = tmp[1]
    src = 2 * (n - 1)
    dst = 2 * (n - 1) + 1
    p[2 * (n - 1)] = (xyr[0][0], xyr[0][1])
    p[2 * (n - 1) + 1] = (xyr[-1][0], xyr[-1][1])
    def is_valid(a, l, r):
        for i in range(l, r):
            if not line_intersection(a, gate[i]):
                return False
        return True
    g = defaultdict(list)
    for l in range(n - 1):
        for i in [2 * l, 2 * l + 1]:
            for r in range(l + 1, n - 1):
                for j in [2 * r, 2 * r + 1]:
                    if is_valid((p[i], p[j]), l + 1, r):
                        x1, y1 = p[i]
                        x2, y2 = p[j]
                        g[i].append((j, sqrt(D2(x1, y1, x2, y2))))
            if is_valid((p[src], p[i]), 0, l):
                x1, y1 = p[src]
                x2, y2 = p[i]
                g[src].append((i, sqrt(D2(x1, y1, x2, y2))))
            if is_valid((p[i], p[dst]), l + 1, n - 1):
                x1, y1 = p[i]
                x2, y2 = p[dst]
                g[i].append((dst, sqrt(D2(x1, y1, x2, y2))))
    
    if is_valid((p[src], p[dst]), 0, n - 1):
        x1, y1 = p[src]
        x2, y2 = p[dst]
        g[src].append((i, sqrt(D2(x1, y1, x2, y2))))
    dist = [[inf] * (2 * n) for i in range(2 * n)]
    for i in range(2 * n):
        dist[i][i] = 0
        for e in g[i]:
            j, d = e
            dist[i][j] = d
    for k in range(2 * n):
        for i in range(2 * n):
            for j in range(2 * n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    print(dist[src][dst])
    return


#main
if __name__ == '__main__':
    while 1:
        n = II()
        if n == 0: break
        solve(n)
