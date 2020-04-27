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
    n, c = LI()
    d0 = [[0, i] for i in range(10)]
    d1 = [[0, i] for i in range(10)]
    for i in range(n):
        a = II()
        if i & 1:
            d1[a - 1][0] += 1
        else:
            d0[a - 1][0] += 1
    d1.sort(reverse=True)
    d0.sort(reverse=True)
    if d0[0][1] == d1[0][1]:
        ans = min(n - d0[0][0] - d1[1][0], n - d0[1][0] - d1[0][0])
    else:
        ans = n - d0[0][0] - d1[0][0]
    print(ans * c)
    return


#main
if __name__ == '__main__':
    solve()
