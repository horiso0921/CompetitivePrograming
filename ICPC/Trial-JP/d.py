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
def LIF(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
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
    h, w = LI()
    if h * w & 1:
        print(0)
        return
    if h == 2:
        dp = [0] * (w + 1)
        dp[0] = 1
        for i in range(w - 1):
            dp[i] %= mod
            dp[i + 1] += dp[i]
            dp[i + 2] += dp[i]
        dp[w] += dp[w - 1]
        print(dp[w] % mod)
    elif h == 3:
        dp = [[0] * 5 for i in range(w + 1)]
        for i in range(w - 1):
            for j in range(5):
                dp[i][j] %= mod
            dp[i + 2][0] += dp[i][0]
            dp[i + 1][1] += dp[i][0]
            dp[i + 1][2] += dp[i][0]
            dp[i + 1][0] += dp[i][1]
            dp[i + 1][3] += dp[i][1]
            dp[i + 1][0] += dp[i][2]
            dp[i + 1][4] += dp[i][2]
            dp[i + 1][1] += dp[i][3]
            dp[i + 1][2] += dp[i][4]
        dp[w][0] = dp[w - 1][1] + dp[w - 1][2]
        print(dp[w][0] % mod)
    elif h == 4:
        dp = [[0] * 5 for i in range(w + 1)]
        for i in range(w - 1):
            for j in range(5):
                dp[i][j] %= mod
            dp[i + 1][0] += dp[i][0]
            dp[i + 2][0] += dp[i][0]
            dp[i + 1][1] += dp[i][0]
            dp[i + 1][2] += dp[i][0]
            dp[i + 1][3] += dp[i][0]
            dp[i + 1][0] += dp[i][1]
            dp[i + 1][3] += dp[i][1]
            dp[i + 1][0] += dp[i][2]
            dp[i + 1][4] += dp[i][2]
            dp[i + 1][0] += dp[i][3]
            dp[i + 1][1] += dp[i][3]
            dp[i + 1][2] += dp[i][4]
        dp[w][0] = dp[w - 1][0] + dp[w - 1][1] + dp[w - 1][2] + dp[w - 1][3]
        print(dp[w][0] % mod)
    else:
        dp = [[0] * (1 << h) for i in range(w + 1)]
        for i in range(w - 1):
            for mask in range(1 << h):
                tmp = []
                tmp1 = []
                for j in range(h - 1):
                    if mask & (1 << j) == 0 and mask & (1 << (j + 1)) == 0:
                        tmp1.append(mask | (1 << j) | (1 << (j + 1)))
                for t in tmp1:
                    for j in range(h):
                        if t & (1 << j) == 0:
                            tmp.append(t | (1 << j))
    




    return


#main
if __name__ == '__main__':
    solve()
