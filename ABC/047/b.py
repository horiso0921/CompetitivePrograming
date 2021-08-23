
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
def B():
    W, H, n = LI()
    wh = [[0, W], [0, H]]
    for _ in range(n):
        x, y, a = LI()
        wha = wh[a > 2]
        x = y if a > 2 else x
        wha[0] = max(x, wha[0]) * (a % 2) or wha[0]
        wha[1] = wha[1] * (a % 2) or min(x, wha[1])
        if wha[0] >= wha[1]:
            print(0)
            return
    print(max(0, (wh[0][1] - wh[0][0]) * (wh[1][1] - wh[1][0])))
    return

