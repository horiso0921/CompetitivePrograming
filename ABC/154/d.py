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
inf = 1e10

#solve
def solve():
    n, k = LI()
    p = LI()
    dp = [0] * n
    bf = list(itertools.accumulate([i for i in range(1001)]))
    for i in range(n):
        dp[i] = bf[p[i]] / p[i]
    ans = 0
    bf = 0
    for i in range(k):
        ans += dp[i]
    bf = ans
    for i in range(k, n):
        bf -= dp[i - k]
        bf += dp[i]
        ans = max(ans, bf)
    print(ans)

    return


#main
if __name__ == '__main__':
    solve()
