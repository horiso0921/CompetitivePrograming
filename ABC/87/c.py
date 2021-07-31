
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
    n = II()
    a = LI()
    dp = [[0] * (n + 1) for i in range(2)]
    for i in range(1, n + 1):
        dp[0][i] += dp[0][i - 1] + a[i - 1]
    a = LI()
    for i in range(1, n + 1):
        dp[1][i] = max(dp[0][i], dp[1][i - 1]) + a[i - 1]
    print(dp[1][-1])
    
    return


class Value_UnionFind():
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.differ_weight = [0] * n
        self.rank = [0] * n

    def root(self,x):
        if x == self.par[x]:
            return x
        r = self.root(self.par[x])
        self.differ_weight[x] += self.differ_weight[self.par[x]]
        self.par[x] = r
        return r

    def weight(self, x):
        self.root(x)
        return self.differ_weight[x]

    def unit(self, x, y, w):
        w += self.weight(x)
        w -= self.weight(y)
        x = self.root(x)
        y = self.root(y)
        if x == y: return False
        if self.rank[x] < self.rank[y]: x, y, w = y, x, -w
        if self.rank[x] == self.rank[y]: self.rank[x] += 1
        self.par[y] = x
        self.differ_weight[y] = w
        return True

    def differ(self, x, y):
        return self.weight(y) - self.weight(x)
