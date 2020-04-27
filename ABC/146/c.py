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
    a, b, x = LI()
    xi = x
    for i in range(9, -1, -1):
        if a * (10 ** i) + b * (i + 1) <= x:
            if i == 9:
                print(10 ** 9)
                return
            x -= (a * (10 ** i) + b * (i + 1))
            x = x // a
            if 10 ** i + x >= 10 ** (i + 1):
                print(10 ** (i + 1) - 1)
                return
            print(10 ** i + x)
            return
    print(0)
    return


#main
if __name__ == '__main__':
    solve()
