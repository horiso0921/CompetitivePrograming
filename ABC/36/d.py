
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
# 木DP
# 難しい 
def D():
    def f(x, pre):
        if dpf[x]:
            return dpf[x]
        tmp = 1
        for i in edg[x]:
            if i == pre:
                continue
            tmp *= g(i, x)
        tmp += g(x, pre)
        dpf[x] = tmp
        return tmp%mod
    def g(x, pre):
        if dpg[x]:
            return dpg[x]
        tmp = 1
        for i in edg[x]:
            if i == pre:
                continue
            tmp *= f(i, x)
        dpg[x] = tmp
        return tmp%mod
    n = II()
    edg = [[] for i in range(n)]
    for _ in range(n-1):
        a, b = LI_()
        edg[a].append(b)
        edg[b].append(a)
    dpf = [0] * n
    dpg = [0] * n
    print(f(0,-1))
    return


