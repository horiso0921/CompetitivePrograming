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
mod = 998244353
inf = 1e10
from functools import lru_cache

@lru_cache(maxsize=100000)
def f(x):
    if x == 2:
        return (1, 0)
    if x == 3:
        return (0, 1)
    res = [0, 0]
    tmp = f(x//2)
    res[0], res[1] = tmp[0], tmp[1]
    tmp = f((x-1)//2 + 1)
    res[0] += tmp[0]
    res[1] += tmp[1]
    return res
#solve
def solve():
    x = II()
    if x == 1:
        print(1)
        return
    res = f(x)
    print(pow(2, res[0], mod) * pow(3, res[1], mod) % mod)
    return


#main
if __name__ == '__main__':
    solve()