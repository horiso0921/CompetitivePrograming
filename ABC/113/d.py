
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
    h, w, k = LI()
    stick = [[0, 0] for i in range(w)]
    stick[0] = [1, 0]
    for i in range(1, w):
        stick[i][0] += stick[i - 1][0] + stick[i - 1][1]
        stick[i][1] += stick[i - 1][0]
    dp1 = [0] * (w + 2)
    dp1[1] = 1
    for i in range(h):
        dp2 = [0] * (w + 2)
        for wi in range(1, w + 1):
            tmp = dp1[wi - 1] * stick[wi - 1][1] * stick[w - wi][0]
            tmp += dp1[wi + 1] * stick[w - wi][1] * stick[wi - 1][0]
            tmp += dp1[wi] * stick[wi - 1][0] * stick[w - wi][0]
            dp2[wi] = tmp
            dp2[wi] %= mod
        dp1 = dp2
    print(dp2[k])

    return

