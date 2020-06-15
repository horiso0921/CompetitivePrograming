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
inf = float("INF")

#solve
def solve():
    n = II()
    a = LI()
    dp = [True] * (10 ** 6 + 1)
    a.sort()
    ans = 0
    d = defaultdict(int)
    for i in a:
        if d[i]:
            d[i] = 0
            ans -= 1
        if dp[i]:
            d[i] = 1
            ans += 1
            dp[i] = False

            for j in range(i * 2, 10 ** 6 + 1, i):
                dp[j] = False
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
