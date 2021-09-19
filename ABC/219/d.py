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

#solve
def solve():
    n = II()
    x,y = LI()
    ab = LIR(n)
    dp = [[inf] * (x+1) for _ in range(y+1)]
    dp[0][0] = 0
    for a,b in ab:
        dp1 = [[inf] * (x+1) for _ in range(y+1)]
        for i in range(x+1):
            for j in range(y+1):
                dp1[j][i] = dp[j][i]
        for i in range(x+1):
            for j in range(y+1):
                if i + a >= x:
                    ni = x
                else:
                    ni = i + a
                if j + b >= y:
                    nj = y
                else:
                    nj = j + b
                dp1[nj][ni] = min(dp1[nj][ni], dp[j][i] + 1)

        dp = dp1
    if dp[-1][-1] == inf:
        print(-1)
    else:
        print(dp[-1][-1])
    return


#main
if __name__ == '__main__':
    solve()