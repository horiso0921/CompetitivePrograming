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

#solve
def solve():
    n = II()
    a = LI()
    ans = 0
    for i in range(1, n+1):
        dp1 = [[0] * i for _ in range(i+1)]
        dp1[0][0] = 1
        for ai in a:
            dp2 = [[0] * i for _ in range(i+1)]
            for j in range(i):
                dp2[i][j] = dp1[i][j]
            for k in range(i):
                for j in range(i):
                    dp2[k+1][(j + ai) % i] += dp1[k][j] 
                    dp2[k+1][(j + ai) % i] %= mod
                    dp2[k][j] += dp1[k][j]
                    dp2[k][j] %= mod
            dp1 = dp2
        ans += dp1[i][0]
        ans %= mod
    print(ans)            
    return


#main
if __name__ == '__main__':
    solve()