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
    def f(m):
        return c * (m - 1) + h * m
    ans = []
    for i in range(II()):
        h, c, t = LI()
        if (h + c) / 2 >= t:
            ans.append(2)
            continue
        l = 10 ** 6
        r = 1
        while l - r > 1:
            m = (r + l) // 2
            if f(m) < t * (2 * m - 1):
                l = m
            else:
                r = m
        fl = abs(f(l) - t * (2 * l - 1)) * (2 * r - 1)
        fr = abs(f(r) - t * (2 * r - 1)) * (2 * l - 1)
        if fl < fr:
            ans.append(l * 2 - 1)
        else:
            ans.append(r * 2 - 1)
    for ai in ans:
        print(ai)
    return


#main
if __name__ == '__main__':
    solve()
