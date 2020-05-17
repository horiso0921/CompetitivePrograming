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
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#solve
def solve():
    t = II()
    ans = [[None for i in range(3)] for i in range(t)]
    for i in range(t):
        l, r = LI()
        L,R = l,r
        fff = l >= r
        if not fff: l, r = r, l
        x = l - r
        ok = 0
        ng = x + 1
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if mid * (mid + 1) <= 2 * x:
                ok = mid
            else:
                ng = mid
        l -= ok * (ok + 1) // 2
        if l == r:
            fff = 1
        x = ok
        okl = 0
        ngl = l + 1
        while ngl - okl > 1:
            mid = (okl + ngl) // 2
            if mid * (x + mid) <= l:
                okl = mid
            else:
                ngl = mid
        okr = 0
        ngr = r + 1
        while ngr - okr > 1:
            mid = (okr + ngr) // 2
            if mid * (x + mid + 1) <= r:
                okr = mid
            else:
                ngr = mid
        ans[i][0] = x + okl + okr
        ans[i][1] = l - okl * (x + okl) if fff else r - okr * (okr + x + 1)
        ans[i][2] = r - okr * (x + okr + 1) if fff else l - okl * (okl + x) 

    for i in range(t):
        print("Case #{}: {} {} {}".format(i + 1, *ans[i]))
    return


#main
if __name__ == '__main__':
    solve()
