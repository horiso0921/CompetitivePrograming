#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
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
def IR(n):
    res = [None] * n
    for i in range(n):
        res[i] = II()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI()
    return res
def FR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR_(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI_()
    return res
def SR(n):
    res = [None] * n
    for i in range(n):
        res[i] = S()
    return res
def LSR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LS()
    return res
mod = 1000000007
inf = float('INF')

#solve
def solve():
    n = II()
    edg = [[] for i in range(n)]
    for _ in range(n-1):
        a, b = LI_()
        edg[a].append(b)
        edg[b].append(a)
    def djk(s):
        dist = [inf] * n
        q = [(0, s)]
        dist[s] = 0
        while q:
            score, p = heappop(q)
            for e in edg[p]:
                if dist[e] > score + 1:
                    dist[e] = score + 1
                    heappush(q, (dist[e], e))
        return dist
    dist1 = djk(0)
    ans = [0, 0]
    for i in range(n):
        if ans[0] < dist1[i]:
            ans = [dist1[i], i]
    dist2 = djk(ans[1])
    ans2 = [0, 0]
    for i in range(n):
        if ans2[0] < dist2[i]:
            ans2 = [dist2[i], i]
    print(ans[1]+1, ans2[1]+1)
    return


#main
if __name__ == '__main__':
    solve()
