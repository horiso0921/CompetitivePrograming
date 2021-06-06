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
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    n = II()
    edg = [[] for i in range(n)]
    ans = 0
    for _ in range(n - 1):
        u,v,w = LI_()
        w += 1
        edg[u].append((v,w))
        edg[v].append((u,w))
    q = deque([0])
    par = [-1] * n
    par[0] = 0
    x = []
    while q:
        p = q.pop()
        for e, w in edg[p]:
            if par[e] == -1:
                par[e] = (p, w)
                q.appendleft(e)
                x.append(e)
    x = x[::-1]
    for i in range(60):
        if i == 0:
            ma = 1
            mab = 1
        else:
            ma *= 2
            mab *= 2
        mab %= mod
        dp1 = [0] * n
        dp0 = [0] * n
        tmp = 0
        for xi in x:
            e, w = par[xi]
            if w & ma:
                dp1[e] += dp0[xi] + 1
                dp0[e] += dp1[xi]
                tmp += (dp0[xi] + 1)
            else:
                dp0[e] += dp0[xi] + 1
                dp1[e] += dp1[xi]
                tmp += dp1[xi]
        for i in range(1, n):
            e, w = par[i]
            if w & ma:
                tmp += (dp0[e] - dp1[i]) * (dp0[i] + 1)
            else:
                tmp += (dp0[e] - dp0[i] - 1) * dp1[i]
        tmp %= mod
        ans += tmp * mab
        ans %= mod
    print(ans)
        

    return


#main
if __name__ == '__main__':
    solve()