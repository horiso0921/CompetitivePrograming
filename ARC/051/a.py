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
    x1, y1, r = LI()
    x2, y2, x3, y3 = LI()
    def f(x, y):
        return (x - x1) ** 2 + (y - y1) ** 2 <= r ** 2

    ans = ["YES", "NO"]
    a1 = x2 <= x1 - r and x3 >= x1 + r and y2 <= y1 - r and y3 >= y1 + r
    a2 = f(x2, y2) and f(x2, y3) and f(x3, y2) and f(x3, y3)
    print(ans[a1])
    print(ans[a2])
    return


#main
if __name__ == '__main__':
    solve()
