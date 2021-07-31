#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
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


n,k = LI()
k *= 8
k1 = (k + 1) * 8
# f = (000)2
# 1bit目 : 0以外の数字が現れたか
# 2bit目 : 0が現れたか
# 3bit目 : 0が現れた後に0以外の数字が現れたか
@lru_cache(None)
def dfs(n, l):
    f = l & 7
    l ^= f
    if n <= 9:
        if f & 4:
            return n + 1
        if f & 1:
            if f & 2:
                return (l <= k) + n
            for i in range(1, n+1):
                if (l * i) > k: break
            else:
                return (l <= k) + n
            return (l <= k) + i - 1
        else:
            if f & 2:
                return n
            for i in range(1, n+1):
                if (l * i) > k: break
            else:
                return n
            return i - 1
    n,r = divmod(n, 10)
    res = dfs(n, l + (4 if f & 4 else f | 2))
    f = 4 if f & 4 else 4 if f & 2 else 1
    for i in range(1, r+1):
        if i * l >= k1:
            res += dfs(n, k1 + f)
        else:
            res += dfs(n, i*l + f)
    n -= 1
    for i in range(r+1, 10):
        if i * l >= k1:
            res += dfs(n, k1 + f)
        else:
            res += dfs(n, i*l + f)
    return res

print(int(dfs(n,8)))

