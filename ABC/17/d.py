
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
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#solve
def D():
    n, m = LI()
    f = IR(n)
    left = [0] * n
    left_f = [0] * (m+1)
    for i in range(n):
        left[i] = max(left[i - 1], left_f[f[i]])
        left_f[f[i]] = i + 1
    dp = [0] * (n + 1)
    dp[0] = 1
    masure = 1
    l = 0
    for i in range(1,n+1):
        for k in range(l,left[i-1]):
            masure -= dp[k]
        l = left[i-1]
        dp[i] += masure
        dp[i] %= mod
        masure += dp[i]
    print(dp[-1])
    return

