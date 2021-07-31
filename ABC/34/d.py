
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
# 解説AC
# 塩何グラムが必要かで優先度をつけられるとかわからんやん
def D():
    def f(mid):
        res = []
        for num, wpi in enumerate(wp):
            w, p = wpi
            res.append((w * (mid - p), num))
        res.sort()
        tmp = [0,0]
        for i in range(k):
            w, p = wp[res[i][1]]
            tmp[0] += w
            tmp[1] += w * p
        if tmp[1] / tmp[0] >= mid:
            return True
        return False
    n, k = LI()
    wp = LIR(n)
    ok = 0
    ng = 100
    for _ in range(100):
        mid = (ok + ng) / 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    print(mid)
