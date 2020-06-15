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
    n, k = LI()
    a = LI()
    for i in range(k):
        bit = [0] * (n+1)
        for j in range(n):
            bit[max(0, j - a[j])] += 1
            bit[min(n, j + a[j] + 1)] -= 1
        f = 0
        bit = list(itertools.accumulate(bit))
        for j in range(n):
            a[j] = bit[j]
            if a[j] < n:
                f = 1
        if f:
            continue
        break
    print(*a)
    return


#main
if __name__ == '__main__':
    solve()
