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
inf = 1e20

#solve
def solve():
    def fx(z):
        for i in range(n):
            if i in v:
                continue
            xi, yi = xy[i]
            x = A - xi
            y = B - yi
            if x ** 2 + y ** 2 > z ** 2:
                return False
        return True
    n = II()
    x = 0
    y = 0
    xy = LIR(n)
    ans = inf
    for i in range(n):
        for j in range(i):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            x = (x2 + x1) / 2
            y = (y2 + y1) / 2
            r = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) / 2
            for k in range(n):
                if i != k and j != k:
                    x3, y3 = xy[k]
                    if (x3 - x) ** 2 + (y3 - y) ** 2 > r ** 2:
                        break
            else:
                ans = min(ans, r)
    # print(ans)
    full = itertools.combinations(range(n), 3)
    for f in full:
        a, b, c = f
        # print(a,b,c)
        axy = xy[a]
        x1, y1 = axy
        bxy = xy[b]
        x2, y2 = bxy
        cxy = xy[c]
        x3, y3 = cxy
        v = [a,b,c]
        a = x1 - x2
        b = y1 - y2
        c = x2 - x3
        d = y2 - y3
        try:
            A = (d * (x1 ** 2 + y1 ** 2 - x2 ** 2 - y2 ** 2) - b * (x2 ** 2 + y2 ** 2 - x3 ** 2 - y3 ** 2)) / (2 * (a * d - b * c))
            B = (-c * (x1 ** 2 + y1 ** 2 - x2 ** 2 - y2 ** 2) + a * (x2 ** 2 + y2 ** 2 - x3 ** 2 - y3 ** 2)) / (2 * (a * d - b * c))
            r = sqrt((x1 - A) ** 2 + (y1 - B) ** 2)
            if fx(r):
                ans = min(ans, r)
        except:
            continue
    
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
