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
def LIR_(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI_()
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

#solve
def solve():
    # n = II()
    # xyp = LIR(n)
    n = 15
    xyp = [[-10000 + 500 * i, -10000 + 500*i, 1000000] for i in range(n)]
    dpx = []
    dpy = []
    for x, y, p in xyp:
        dpx.append(x)
        dpy.append(y)
    dpx.sort()
    dpy.sort()
    dpx = sorted(list(set(dpx)))
    dpy = sorted(list(set(dpy)))
    masks = defaultdict(list)
    for i in range(1 << n):
        t = i
        b = 0
        while i:
            b += i & 1
            i >>= 1
        key = masks[b].append(t)
    ans = [inf] * n
    XX = 1 << len(dpx)
    YY = 1 << len(dpy)
    for j in range(n):
        for i in range(j + 1):
            if i > len(dpx):
                break
            if j - i > len(dpy):
                continue
            for maskx in masks[i]:
                if maskx - XX >= 0:
                    break
                for masky in masks[j - i]:
                    if masky - YY >= 0:
                        break
                    tmp = 0
                    tmpx = []
                    tmpy = []
                    for v in range(n):
                        if 1 << v & maskx:
                            tmpx.append(dpx[v])
                        if 1 << v & masky:
                            tmpy.append(dpy[v])
                    for x, y, p in xyp:
                        t = min(abs(x), abs(y)) * p
                        for tx in tmpx:
                            if abs(tx - x) * p < t:
                                t = abs(tx - x) * p
                        for ty in tmpy:
                            if abs(ty - y) * p < t:
                                t = abs(ty - y) * p
                        tmp += t
                    if ans[j] > tmp:
                        ans[j] = tmp
                        print(ans)
    for a in ans:
        print(a)
    print(0)


    return


#main
if __name__ == '__main__':
    solve()
