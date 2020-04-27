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
    s = S()
    i = II()
    print(s[i-1])
    return

#B
def B():
    a, b, c = LI()
    print(((a * b % mod) * c % mod) % mod)
    return

#C
def C():
    n = II()
    a = LI()
    ans = []
    for i in range(n):
        ans.append((a[i], i+1))
    ans.sort(reverse=True)
    for _, a in ans:
        print(a)
    return

# D
# 解説AC
# BITDP、トポロジカルソート
# BITで使用可能な頂点集合を保持する
# 使用可能な頂点集合の下使用可能な頂点集合へ
# の有向辺が存在しない頂点のやつを足す
# これもらうDP? 
def D():
    n, m = LI()
    edg = [[] for _ in range(n)]
    dp = [0 for i in range(1 << n)]
    dp[0] = 1
    for _ in range(m):
        x, y = LI_()
        edg[y].append(x)
    for i in range(1, 1 << n):
        for k in range(n):
            if (i >> k) & 1:
                for e in edg[k]:
                    if (i >> e) & 1:
                        break
                else:
                    dp[i] += dp[i ^ (1 << k)]
    print(dp[-1])

    return

#Solve
if __name__ == '__main__':
    D()
