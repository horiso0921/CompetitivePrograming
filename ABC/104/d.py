
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
def D_():
    N, X = LI()
    def dfs(n, x):
        #print(n, x)
        if x == 1 and n > 0:
            return 0 
        elif x < 2 ** (n + 1) - 1:
            return dfs(n - 1, x - 1)
        elif x == 2 ** (n + 1) - 1:
            return 2 ** n 
        elif x == 2 ** (n + 2) - 3:
            return 2 ** (n + 1) - 1
        else:
            return dfs(n - 1, x - 2 ** (n + 1) + 1) + 2 ** n 
    a = dfs(N, X)
    print(a)
    return

def D():
    s = S()
    dp = [0] * 3
    s = s[::-1]
    x = 1
    for i, si in enumerate(s):
        if si == "A":
            dp[0] = (dp[0] + dp[1]) % mod
        elif si == "B":
            dp[1] = (dp[1] + dp[2]) % mod
        elif si == "C":
            dp[2] = (dp[2] + x) % mod
        else:
            dp[0] = (dp[0] * 3 + dp[1]) % mod
            dp[1] = (dp[1] * 3 + dp[2]) % mod
            dp[2] = (dp[2] * 3 + x) % mod
            x *= 3
            x %= mod
    print(dp[0])

