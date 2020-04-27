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
    a, b = LI()
    print(min(b-1,a-b))
    return

#B
def B():
    n = II()
    ans = inf
    for i in range(1, int(n ** 0.5) + 1):
        b = n // i
        ans = min(ans, abs(i - b) + n - i * b)
    print(ans)
    return

#C
def C():
    n = II()
    a = LI()
    dp = [inf] * (n)
    dp[0] = 0
    for i in range(n - 1):
        if i != n - 2:
            dp[i + 2] = min(dp[i + 2], dp[i] + abs(a[i] - a[i + 2]))
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(a[i] - a[i + 1]))
    print(dp[-1])
    return

#D
def D():
    def find(a):
        if a == par[a]:
            return a
        par[a] = find(par[a])
        return par[a]

    def unite(a, b):
        a = find(a)
        b = find(b)
        if rank[a] < rank[b]: a, b = b, a
        if a == b: return
        par[b] = a
        rank[a] += rank[b]
    
    n, m = LI()
    rank = [1] * n
    par = [i for i in range(n)]
    lis = []
    for _ in range(m):
        a, b, y = LI_()
        lis.append((y, a, b))
    q = II()
    for i in range(q):
        v, w = LI_()
        lis.append((w, i + n, v))
    lis.sort(reverse = True)
    ans = [None] * q
    for l in lis:
        if l[1] >= n:
            ans[l[1] - n] = rank[find(l[2])]
        else:
            unite(l[1], l[2])
    for a in ans:
        print(a)
    return


#Solve
if __name__ == '__main__':
    D()
