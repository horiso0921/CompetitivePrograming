#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
sys.setrecursionlimit(2*10**6)
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
    for _ in range(n-1):
        u,v = LI_()
        edg[u].append(v)
        edg[v].append(u)

    ans = [[n,1] for i in range(n)]
    d = [1]
    def dfs(p, pre):
        if pre != -1 and len(edg[p]) == 1:
            ans[p] = [d[0], d[0]]
            d[0] += 1
            return
        ma = 1
        mi = n
        for e in edg[p]:
            if e != pre:
                dfs(e, p)
                ma = max(ma, ans[e][1])
                mi = min(mi, ans[e][0])
        ans[p] = [mi, ma]
        return 
    dfs(0, -1)
    for a in ans:
        print(*a)
    return


#main
if __name__ == '__main__':
    solve()