
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
def F():
    n,m = LI()
    edg = [[] for i in range(n)]
    redg = [[] for i in range(n)]
    
    for _ in range(m):
        a, b = LI_()
        edg[a].append(b)
        redg[b].append(a)

    def dijkstra(start):
        dist = [inf] * n
        dist[start] = 0
        q = [(0,start)]
        while q:
            du, u = heappop(q)
            for i in edg[u]:
                if du + 1 < dist[i]:
                    dist[i] = du + 1
                    heappush(q, (du + 1, i))
        return dist
    
    d = [None] * n
    for i in range(n):
        d[i] = dijkstra(i)

    tmp = inf
    tt = None
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if tmp > d[i][j] + d[j][i]:
                tt = (i, j)
                tmp = d[i][j] + d[j][i]

    if tmp != inf:
        print(tmp)
        s, g = tt
        ans1 = [s]
        ans2 = [g]
        q = deque([s])
        while q:
            a = q.pop()
            for ai in redg[a]:
                if g != ai and d[g][ai] + 1 == d[g][a]:
                    ans1.append(ai)
                    q.append(ai)
                    break
        q = deque([g])
        while q:
            a = q.pop()
            for ai in redg[a]:
                if s != ai and d[s][ai] + 1 == d[s][a]:
                    ans2.append(ai)
                    q.append(ai)
                    break
        ans = ans1 + ans2
        for a in ans:
            print(a+1)

    else:
        print(-1)
    return

def F_():
    n, m = LI()
    edg = [[] for i in range(n)]
    for a, b in LIR_(m):
        edg[a].append(b)
    f = 0
    for i in range(n):
        q = deque()

