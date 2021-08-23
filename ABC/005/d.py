
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
n = int(input())
feild = [list(map(int, input().split())) for i in range(n)]
num_tenin = int(input())
tenin = [int(input()) for i in range(num_tenin)]

ans = [0 for i in range(n ** 2 + 1)]

dp = [[0 for i in range(n+1)] for k in range(n+1)]
for i in range(n):
    for k in range(n):
        dp[k][i] = dp[k - 1][i] + dp[k][i - 1] - dp[k - 1][i - 1] + feild[k][i]
        ans[(k+1)*(i+1)] = max(ans[(k+1)*(i+1)], dp[k][i])

for tate in range(n):
    for yoko in range(n):
        for tate_haba in range(1, n - tate + 1):
            for yoko_haba in range(1, n - yoko + 1):
                bf = dp[tate + tate_haba - 1][yoko + yoko_haba - 1] - dp[tate - 1][yoko + yoko_haba - 1] - dp[tate + tate_haba - 1][yoko - 1] + dp[tate - 1][yoko - 1]
                ans[yoko_haba * tate_haba] = max(ans[tate_haba * yoko_haba], bf)
                for i in range(1, n ** 2 + 1):
                    ans[i] = max(ans[i], ans[i - 1])
for ten in tenin:
    print(ans[ten])