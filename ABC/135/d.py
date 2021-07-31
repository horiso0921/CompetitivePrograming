
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
    s = S()
    s = s[::-1]
    dp = [[0] * 13 for _ in range(len(s))]
    remain = 1
    if s[0] == "?":
        for i in range(10):
            dp[0][i] = 1
    else:
        dp[0][int(s[0])] = 1
    for i in range(1, len(s)):
        remain = (remain * 10) % 13
        dpi = dp[i]
        dpi1 = dp[i-1]
        if s[i] == "?":
            for k in range(10):
                for j in range(13):
                    dpi[(j + remain * k) % 13] += dpi1[j]
                    dpi[(j + remain * k) % 13] %= mod
        else:
            for j in range(13):
                dpi[(j + remain * int(s[i])) % 13] += dpi1[j]
    print(dp[-1][5])
    return

