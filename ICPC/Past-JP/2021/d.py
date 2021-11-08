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

#solve
def solve(n):
    b = LI()
    MAX = sum(b) // 2 + 3
    dp = [[0] * MAX for k in range(MAX)]
    dp[0][0] = 1
    for i in range(n):
        ndp = [d[:] for d in dp]
        bi = b[i]
        for j in range(MAX):
            for k in range(MAX):
                if j >= bi:
                    ndp[j][k] |= dp[j-bi][k]
                if k >= bi:
                    ndp[j][k] |= dp[j][k - bi]
        dp = ndp
    # print(dp)
    sb = sum(b)
    ans = 0
    for x in range(MAX):
        for y in range(MAX):
            z = sb - x - y
            if z < 0:
                continue
            if dp[x][y]:
                ans = max(ans, min(x,y,z))
    print(ans,flush=True)
    return


#main
if __name__ == '__main__':
    while 1:
        n = II()
        if n == 0:
            break
        solve(n)