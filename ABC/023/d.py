
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
    def f(x):
        T = [0] * n
        for h, s in hs:
            t = (x - h) // s
            if t < n:
                T[t] += 1
        y = 0
        for num, t in enumerate(T):
            y += t
            if num + 1 < y:
                return False
        return True
    n = II()
    hs = LIR(n)
    l = 0
    r = 0
    for h, s in hs:
        l = max(l, h - 1)
        r = max(r, h + (n - 1) * s)
    while r - l > 1:
        m = (l + r) // 2
        if f(m):
            r = m
        else:
            l = m
    print(r)
    
    return

