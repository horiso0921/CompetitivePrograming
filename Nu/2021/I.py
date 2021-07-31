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
inf = float("inf")

from functools import lru_cache
@lru_cache(None)
def dfs1(a, mask, tmp):
    if tmp:
        if a <= 9:
            return a
        
        a, r = divmod(a, 10)
        res = 0
        for i in range(10):
            res = max(res, i + dfs1(a - (r < i), mask | 1 << i, tmp - ((mask >> i & 1) ^ 1)) * 10)
        return res
    else:
        if a <= 9:
            for i in range(a, -1, -1):
                if mask & 1 << i:                 
                    return i
            return 0
        
        a, r = divmod(a, 10)
        res = 0
        for i in range(10):
            if mask & 1 << i:
                res = max(res, i + dfs1(a - (r < i), mask | 1 << i, 0) * 10)
        return res

@lru_cache(None)
def dfs2(a, mask, tmp):
    if tmp:
        if a <= 9:
            return a
        
        a, r = divmod(a, 10)
        res = inf
        for i in range(10):
            res = min(res, i + dfs2(a + (r > i), mask | 1 << i, tmp - ((mask >> i & 1) ^ 1)) * 10)
        return res
    
    else:
        if a <= 9:
            for i in range(a, 10):
                if mask & 1 << i:                 
                    return i
            for i in range(1, 10):
                if mask & 1 << i:                 
                    return i * 10 + i
            return 0
        
        a, r = divmod(a, 10)
        res = inf
        for i in range(1, 10):
            if mask & 1 << i:
                res = min(res, i + dfs2(a + (r > i), mask | 1 << i, 0) * 10)
        return res
a, k = LI()
print(a-dfs1(a,0,k))
print(dfs2(a,0,k)-a)
