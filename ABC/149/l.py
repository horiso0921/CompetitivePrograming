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
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10


from heapq import heappush, heappop

def Dijkstra(num, start, vedge):
    """ vedge は DAG の 重みとして vedge[from] = (to, value)　としておくこと """
    """ DAGでない場合は vedge[from] と vedge[to] の両方を作ること """
    """ dist[i] は start から i までの最短距離 """

    dist = [[float("inf"),-1] for i in range(num)]
    dist[start] = [0, -1]
    q = [[dist[start][0], start]]
    while q:
        du, u = heappop(q)
        for j, k in vedge[u]:
            if dist[j][0] > du + k:
                dist[j][0] = du + k
                dist[j][1] = u
                heappush(q, [dist[j][0], j])
    return dist


#solve
def solve():
    n = II()
    edg = [[] for i in range(n)]
    for i in range(14):
        a, b, cost = LI_()
        cost += 1
        edg[a].append((b, cost))
    ans = Dijkstra(n, 0, edg)
    p = [-1] * n
    for i in range(n):
        p[i] = ans[i][1]
    print(ans)
    ans = []
    # print(p)
    for i in range(1,n):
        tmp = []
        t = i
        while t != -1:
            tmp.append(t)
            t = p[t]
        ans.append(tmp[::-1])
    print("\n".join(map(str, ans)))
    return


#main
if __name__ == '__main__':
    solve()

