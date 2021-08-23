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
    n,k = LI()
    down = []
    x = LI()
    d = defaultdict(int)
    for i, xi in enumerate(x):
        d[xi] = i+1
    for i in range(n):
        if len(down) < k:
            heappush(down, -x[i])
            if len(down) == k:
                p = -heappop(down)
                print(d[p])
                heappush(down,-p)
        else:
            p = -heappop(down)
            if p > x[i]: p = x[i]
            heappush(down,-p)
            p = -heappop(down)
            print(d[p])
            heappush(down, -p)

    return


#main
if __name__ == '__main__':
    solve()
