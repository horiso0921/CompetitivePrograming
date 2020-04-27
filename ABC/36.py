#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**7)
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
    a, b = LI()
    print((b-1)//a+1)
    return

#B
def B():
    n = II()
    s = SR(n)
    for i in range(n):
        b = deque()
        for j in range(n):
            b.appendleft(s[j][i])
        print("".join(b))
    return

#C
def C():
    n = II()
    d = defaultdict(int)
    a = IR(n)
    b = list(set(a))
    b.sort()
    for num, bi in enumerate(b):
        d[bi] = num
    for i in a:
        print(d[i])

    return

# D
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


#Solve
if __name__ == '__main__':
    D()
