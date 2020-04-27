#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10 ** 9)
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
inf = float('INF')

#solve
def solve():
    n, K = LI()
    edg = [[] for i in range(n)]
    for _ in range(n - 1):
        u, v = LI_()
        edg[u].append(v)
        edg[v].append(u)
    dp = [0] * n
    rank = [0] * n
    q = deque()
    q.append((0,-1))
    l = []
    while q:
        p, pre = q.popleft()
        f = 0
        for e in edg[p]:
            if e != pre:
                f = 1
                rank[e] = rank[p] + 1
                q.append((e, p))
        if f:
            continue
        heappush(l, (-rank[p], p))
    c = [1] * n
    while l:
        r, p = heappop(l)
        r = -r
        for e in edg[p]:
            if r - 1 == rank[e]:
                dp[e] += dp[p] + 1
            if c[e]:
                c[e] = 0
                heappush(l, (-(r - 1), e))

    ans = list(map(lambda x: x[0] - x[1], zip(dp, rank)))
    ans.sort()
    print(sum(ans) - sum(ans[:K]))
    return


#main
if __name__ == '__main__':
    solve()
