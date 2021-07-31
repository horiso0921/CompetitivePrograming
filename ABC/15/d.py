
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
    W = II()
    N, K = LI()
    ab = LIR(N)
    dp = [[0 for i in range(W + 1)] for l in range(K + 1)]
    for num, ab_ in enumerate(ab):
        a = ab_[0]
        b = ab_[1]
        for w in range(W, -1, -1):
            for k in range(K, 0, -1):
                if a <= w:
                    dp[k][w] = max(dp[k][w], dp[k - 1][w - a] + b)
                else:
                    dp[k][w] = dp[k][w] 

    print(dp[K][W])
              
 
    return
 
