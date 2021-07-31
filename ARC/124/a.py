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
mod = 998244353
inf = 1e10

#solve
def solve():
    n,K = LI()
    dp = [0] * n
    ck = []
    for i in range(K):
        i += 1
        c,k = LS()
        if c == "L":
            dp[int(k)-1] += 1
            ck.append(int(k)-1)
        else:
            dp[0] += 1
            ck.append(int(k)-1)
            dp[int(k)-1] -= 1
    dp = list(itertools.accumulate(dp))
    ck.sort()
    x = 0
    ans = 1
    for i in range(n):
        if x < K:
            if ck[x] == i:
                x += 1
            else:
                ans *= dp[i]
                ans %= mod
        else:
            ans *= dp[i]
            ans %= mod
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()