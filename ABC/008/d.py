
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

w, h = map(int, input().split())
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

#辞書版

d = {}

def dp(xle, ydo, xri, yup):
    if (xle, ydo, xri, yup) in d:
        return d[(xle, ydo, xri, yup)]
    
    bf = 0
    for x, y in xy:
        if xle <= x <= xri and ydo <= y <= yup:
            bf = max(bf, xri - xle + yup - ydo + 1 + dp(x + 1, y + 1, xri, yup) + dp(xle, y + 1, x - 1, yup) + dp(xle, ydo, x - 1, y - 1) + dp(x + 1, ydo, xri, y - 1))
    d[(xle, ydo, xri, yup)] = bf
    return bf


print(dp(1,1,w,h))