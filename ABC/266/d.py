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
inf = float("inf")

#solve
def solve():
    n = II()
    dp = [-inf] * 5
    que = [None for _ in range(10 ** 5 + 1)]
    dp[0] = 0
    for _ in range(n):
        t,x,a = LI()
        que[t] = (x, a)
    
    for i in que:
        if i != None:
            dp[i[0]] += i[1]
        ndp = dp[:]
        for i in range(5):
            if 0 <= i - 1 < 5:
                ndp[i - 1] = max(ndp[i - 1], dp[i])
            if 0 <= i + 1 < 5:
                ndp[i + 1] = max(ndp[i + 1], dp[i])
        dp = ndp
    print(max(dp))
    return


#main
if __name__ == '__main__':
    solve()