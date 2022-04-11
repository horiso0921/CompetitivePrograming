#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
sys.setrecursionlimit(10**7)
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
    @lru_cache(maxsize=10**5)
    def game(n, one, two):
        if one == 0 and two == 0:
            return False
        n += 1
        n %= 3
        if n == 0:
            two += 1
        a = True
        b = True
        c = True
        if two >= 1:
            a = game(n, one+1, two-1) 
            b = game(n, one, two-1)
        if one >= 1:
            c = game(n, one-1, two)
        # print(a,b,c, n, one, two)
        if a & b & c:
            return False
        else:
            return True
    for n in range(1, 50):
        # n = II()
        print(game(0, 0, n))
    return


#main
if __name__ == '__main__':
    solve()