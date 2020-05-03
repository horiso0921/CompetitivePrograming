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
inf = float("INF")

#solve
def solve():
    n, m = LI()
    ans = [[i + 1, None] for i in range(m)]
    v = n
    j = m + 1
    d = defaultdict(int)
    d[0] = 1
    d[n] = 1
    for i in range(m - 1, -1, -1):
        while d[n - (j - ans[i][0])]: j += 1
        if (j - ans[i][0]) * 2 == n: j += 1
        d[j - ans[i][0]] = 1
        ans[i][1] = j
        j += 1
    for a in ans:
        print(*a)
    return


#main
if __name__ == '__main__':
    solve()
