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
def IR(n):
    res = [None] * n
    for i in range(n):
        res[i] = II()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI()
    return res
def FR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR_(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI_()
    return res
def SR(n):
    res = [None] * n
    for i in range(n):
        res[i] = S()
    return res
def LSR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LS()
    return res
mod = 1000000007
inf = float('INF')

#solve
def solve():
    n = II()
    a = LI()
    dp = [[None for i in range(n + 1)] for i in range(n + 1)]
    for i in range(n):
        dp[i][i + 1] = [a[i], a[i], 1]
        dp[i + 1][i] = [a[i], a[i], 1]
    for i in range(2, n + 1):
        for l in range(n - i + 1):
            tmp = [-inf, inf, inf]
            r = l + i
            dpl = dp[l]
            dpr = dp[r]
            for m in range(l + 1, r):
                lm = dpl[m]
                mr = dpr[m]
                lr = lm[2] + mr[2] - (lm[1] == mr[0])
                if lr < tmp[2]:
                    tmp[2] = lr
                    if lm[1] == mr[0]:
                        if lm[2] == 1:
                            tmp[0] = lm[0] + 1
                        else:
                            tmp[0] = lm[0]
                        if mr[2] == 1:
                            tmp[1] = mr[1] + 1
                        else:
                            tmp[1] = mr[1]
                    else:
                        tmp[0] = lm[0]
                        tmp[1] = mr[1]
            dp[l][r] = tmp
            dp[r][l] = tmp
    print(dp[0][n][2])
    return


#main
if __name__ == '__main__':
    solve()
