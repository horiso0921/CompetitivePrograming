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
def solve(x):
    y = S()
    a = II()
    e = II()
    s = II()
    r = II()
    tx = x * x
    le = len(x)
    for i in range(len(x)):
        x = tx[i:le+i]
        dp = [[inf] * (len(y)+1) for _ in range(len(x) + 1)]

        lx = len(x)
        ly = len(y)

        for i in range(lx+1):
            dp[i][0] = i * e
        for i in range(ly+1):
            dp[0][i] = i * a

        for i in range(1,lx+1):
            for j in range(1, ly+1):
                re = s if x[i-1] != y[j-1] else 0
                dp[i][j] = min(
                    dp[i][j],
                    dp[i-1][j] + e,
                    dp[i][j-1] + a,
                    dp[i-1][j-1] + re)
    
    print(dp[-1][-1])
    return


#main
if __name__ == '__main__':
    while 1:
        x = S()
        if x == "#":
            break
        solve(x)