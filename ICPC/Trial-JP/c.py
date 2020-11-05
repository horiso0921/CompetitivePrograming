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
def LIF(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
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
from heapq import heappush, heappop

def Dijkstra(num, start, vedge):
    """ vedge は DAG の 重みとして vedge[from] = (to, value)　としておくこと """
    """ DAGでない場合は vedge[from] と vedge[to] の両方を作ること """
    """ dist[i] は start から i までの最短距離 """

    dist = [float("inf") for i in range(num)]
    dist[start] = 0
    q = [[dist[start], start]]
    while q:
        du, u = heappop(q)
        for j, k in vedge[u]:
            if dist[j] > du + k:
                dist[j] = du + k
                heappush(q, [dist[j], j])
    return dist


#solve
def solve():
    h, w = LI()
    px, py, qx, qy = LI_()
    s = SR(h)
    dist = [[[inf] * 4 for i in range(w)] for j in range(h)]
    move = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    dist[px][py][1] = 0
    q = [(0, (px, py, 1))]
    while q:
        du, u = heappop(q)
        nx, ny, nd = u
        nd -= 1
        nd %= 4
        mx, my = move[nd]
        mx += nx
        my += ny
        if 0 <= my < w and 0 <= mx < h:
            if s[mx][my] == "." and dist[mx][my][nd] > du + 1:
                dist[mx][my][nd] = du + 1
                heappush(q, (du + 1, (mx, my, nd)))
                continue
        for i in range(3):
            nd += 1
            nd %= 4
            mx, my = move[nd]
            mx += nx
            my += ny
            if 0 <= my < w and 0 <= mx < h:
                if s[mx][my] == "." and dist[mx][my][nd] > du + 1:
                    dist[mx][my][nd] = du + 1
                    heappush(q, (du + 1, (mx, my, nd)))
                    break

    ans = min(dist[qx][qy])
    print(-1 if ans == inf else ans)
    return


#main
if __name__ == '__main__':
    solve()
