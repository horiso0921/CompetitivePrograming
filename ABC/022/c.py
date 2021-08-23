
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
inf = float('INF')

#solve
def C():
    n, m = LI()
    vedg = defaultdict(lambda: inf)
    edge = [[] for i in range(n)]
    for _ in range(m):
        u, v, l = LI_()
        l += 1
        vedg[(u, v)] = l
        vedg[(v, u)] = l
        edge[v].append(u)
        edge[u].append(v)
    if len(edge[0]) < 2:
        print(-1)
        return
    ans = inf

    #ワーシャルフロイド
    field = [[None for __ in range(n)] for _ in range(n)]
    for u in range(1,n):
        for v in range(1,n):
            field[u][v] = vedg[(u,v)]

    for k in range(1,n):
        for i in range(1,n):
            for j in range(1,n):
                if field[i][j] > field[i][k] + field[k][j]:
                    field[i][j] = field[i][k] + field[k][j]

    for i in edge[0]:
        for k in edge[0]:
            if i == k:
                continue
            ans = min(ans, field[k][i] + vedg[(i, 0)] + vedg[(0, k)])
    if ans == inf:
        print(-1)
    else:
        print(ans)
    return

