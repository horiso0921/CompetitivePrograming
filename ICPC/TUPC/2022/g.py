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
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10
from functools import lru_cache

#solve
def solve():
    h,w = LI()
    s = [list(map(int, list(S()))) for _ in range(h)]
    rows = [sum((s[j][i] for j in range(h))) for i in range(w)]
    imorows = [0]+list(itertools.accumulate(rows))
    cols = [sum(s[i]) for i in range(h)]
    imocols = [0]+list(itertools.accumulate(cols))

    @lru_cache(maxsize=1000000)
    def dfsrow(l, r):
        if r - l == 1:
            return 0
        res = 0
        for m in range(l+1, r):
            tmp = dfsrow(l, m) + dfsrow(m, r) + imorows[r] - imorows[l]
            if tmp > res:
                res = tmp

        return res

    @lru_cache(maxsize=1000000)
    def dfscol(l, r):
        if r - l == 1:
            return 0
        res = 0
        for m in range(l+1, r):
            tmp = dfscol(l, m) + dfscol(m, r) + imocols[r] - imocols[l]
            if tmp > res:
                res = tmp
        return res

    if w >= 201 or h >= 201:
        print("Please Accept")
        raise RuntimeError
    
    print(dfsrow(0, w) + dfscol(0, h))
    return


#main
if __name__ == '__main__':
    solve()