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
    n,K = LI()
    p = LI()
    q = LI()
    dp = defaultdict(int)
    for pi,qi in zip(p,q):
        dp[(pi,qi,1)] = 1 
        for i in range(pi+1, n+1):
            for j in range(qi+1, n+1):
                for k in range(K):
                    dp[(i,j,k+1)] += dp[(i,j,k)]
                    dp[(i,j,k+1)] %= mod
    ans = 0
    print(dp)
    for i in range(n+1):
        for j in range(n+1):
            ans += dp[(i,j,K)]
            ans %= mod
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()