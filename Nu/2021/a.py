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
inf = 1e10

from functools import lru_cache 

#solve
def solve():
    @lru_cache(None)
    def dfs(n, k):
        if n < 10:
            if k == 0:
                return 1
            elif k == 1:
                return n
            else:
                return 0
        n, m = n // 10, n % 10
        return dfs(n, k) + dfs(n, k - 1) * m + dfs(n - 1, k - 1) * (9 - m)
    n,k = IR(2)
    print(dfs(n,k))
    return


#main
if __name__ == '__main__':
    solve()