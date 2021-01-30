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
def LFR(n): return [LF() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e20

#solve
def solve():
    n,m = LI()
    edg = [[] for i in range(n)]
    
    for _ in range(m):
        a,b = LI_()
        edg[a].append(b)
        edg[b].append(a)
    
    k = II()
    c = LI_()
    
    dp = [[inf] * (1 << k) for i in range(k)]
    q = []
    
    bi = [1 << i for i in range(k)]
    for i in range(k):
        dp[i][bi[i]] = 1
        q.append((1, i, bi[i]))

    dist = [[inf] * n for i in range(k)]
    
    for i in range(k):
        x = c[i]
        qq = deque([x])
        dist[i][x] = 0
        disti = dist[i]
        while qq:
            y = qq.popleft()
            for e in edg[y]:
                if disti[y] + 1 < disti[e]:
                    disti[e] = disti[y] + 1
                    qq.append(e)

    end = (1 << k) - 1
    for mask in range(1 << k):
        tmp1 = []
        tmp2 = []
        for i in range(k):
            if mask & bi[i]:
                tmp1.append(i)
            else:
                tmp2.append(i)
        for i in tmp1:
            s = dp[i][mask]
            for j in tmp2:
                if dp[j][mask | bi[j]] > s + dist[i][c[j]]:
                    dp[j][mask | bi[j]] = s + dist[i][c[j]]
    ans = inf
    for i in range(k):
        ans = min(ans, dp[i][-1])
    if ans == inf:
        print(-1)
    else:
        print(ans)
    return


#main
if __name__ == '__main__':
    solve()