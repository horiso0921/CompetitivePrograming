#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    a = II()
    ans = 0
    for i in range(1,a):
        for k in range(1,a):
            if i + k == a:
                ans = max(ans, i * k)
    print(ans)
    return

#B
def B():
    n = II()
    x = IR(n)
    x.sort()
    ans = 0
    t = 0
    for i in x:
        ans += i ** 2 * [1, -1][t]
        t ^= 1
    print(abs(ans*math.pi))
    return

#C
def C():
    n = II()
    b = [[] for i in range(n)]
    for i in range(1,n):
        bi = II()
        b[bi - 1].append(i)
    def dfs(now, pre):
        big = 0
        small = inf
        f = True
        for n in b[now]:
            if n != pre:
                x = dfs(n, now)
                big = max(x, big)
                small = min(x, small)
                f = False
        if f:
            return 1
        return big + small + 1
    print(dfs(0,-1))
        
    return

#D
def D():
    def f(t):
        return a * t + b * math.sin(c * t * math.pi)
    a, b, c = LI()
    ok = 99 // a + 1
    ng = 0
    while 1:
        t = (ok + ng) / 2
        ft = f(t)
        if abs(ft - 100) <= 10 ** (-6):
            print(t)
            return
        if ft > 100:
            ok = t
        if ft < 100:
            ng = t
    return

#Solve
if __name__ == '__main__':
    D()
