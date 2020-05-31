#!/usr/bin/env python3
import itertools
import math
import random
import sys
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from heapq import heappop, heappush

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
    ans = []
    for i in range(II()):
        n, m, k = LI()
        x = min(m, n // k)
        m -= x
        if m:
            y = (m - 1) // (k - 1) + 1
        else:
            y = 0
        ans.append(x - y)
    for ai in ans:
        print(ai)
    return


#main
if __name__ == '__main__':
    solve()
