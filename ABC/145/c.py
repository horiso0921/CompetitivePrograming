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
def solve():
    n = II()
    xy = LIR(n)
    full = itertools.permutations(range(n), n)
    tmp = 0
    ans = 0
    for fu in full:
        i = 0
        bx, by = 0, 0
        for f in fu:
            if i == 0:
                bx, by = xy[f][0], xy[f][1]
                i = 1
                continue
            x, y = xy[f][0], xy[f][1]
            ans += sqrt((bx - x) ** 2 + (by - y) ** 2)
        tmp += 1
    print(ans/tmp)

    return


#main
if __name__ == '__main__':
    solve()
