
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
def C():
    n, a = LI()
    x = LI()
    sumx = [0] * n
    for i in range(n):
        sumx[i] = sumx[i - 1] + x[i]
    dp = [[[0] * (n+1) for i in range(sumx[-1] + 1)] for i in range(n)]
    for i in range(n):
        dp[i][x[i]][1] = 1
    for i in range(1, n):
        for s in range(sumx[i] + 1):
            for k in range(1, i + 2):
                if  s >= x[i]:
                    dp[i][s][k] += dp[i - 1][s - x[i]][k - 1]
                dp[i][s][k] += dp[i - 1][s][k]
    ans = 0
    for i in range(1, n + 1):
        if a * i > sumx[-1]:
            break
        ans += dp[-1][a * i][i]
    print(ans)
    return

