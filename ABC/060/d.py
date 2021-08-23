
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
    n, W = LI()
    wv = LIR(n)
    wv.sort()
    dp = [-inf] * ((3 * n + 1) * n + 1)
    dp[0] = 0
    minw =  wv[0][0]
    if minw <= 3 * n:
        for w, v in wv:
            for i in range((3 * n + 1) * n, w - 1, -1):
                dp[i] = max(dp[i - w] + v, dp[i])
        print(max(dp[:W + 1]))
    else:
        for w, v in wv:
            w -= minw
            for i in range(min(W // minw, n - 1), 0, -1):
                for k in range(3 * n, w - 1, -1):
                    dp[(3 * n + 1) * i + k] = max(dp[(3 * n + 1) * (i - 1) + k - w] + v, dp[(3 * n + 1) * i + k])
        print(max(dp[:W // minw * (3 * n + 1) + W % minw + 1]))
    return

