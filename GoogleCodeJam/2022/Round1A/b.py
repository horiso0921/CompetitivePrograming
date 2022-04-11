#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math, random
from typing import Tuple
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

#solve
def solve():
    for I in range(II()):
        I += 1
        n = II()
        if n == -1:
            return
        a = []
        i = 1
        while i <= 10 ** 9:
            a.append(i)
            i *= 2
        for i in range(10 ** 9, 10 ** 9 - 100 + len(a), -1):
            a.append(i)
        # print(len(a))
        print(*a, flush=True)
        l = LI()
        if -1 in l:
            return
        s = sum(a) + sum(l)
        la = sorted(a + l)[::-1]
        s //= 2
        i = 0
        ans = []
        while s >= 10 ** 9:
            s -= la[i]
            ans.append(la[i])
            i += 1
        i = 0
        while s:
            if s & 1:
                ans.append(pow(2, i))
            s //= 2
            i += 1
        print(*ans, flush=True)
                
            
    return


#main
if __name__ == '__main__':
    solve()