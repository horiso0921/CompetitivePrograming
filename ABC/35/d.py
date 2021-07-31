
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
# 解説AC
# 1→全点はdijkstraで全点→1は全部の辺を逆向きにさせて1→全点で出せる
# 気づきたいなぁ
def D():
    def dijkstra(s, d):
        dist = [inf] * n
        dist[s] = 0
        q = [[dist[s], s]]
        while q:
            dis, now = heappop(q)
            for nex, val in d[now]:
                if dis + val < dist[nex]:
                    dist[nex] = dis + val
                    heappush(q, [dist[nex], nex])
        return dist
    n, m, t = LI()
    A = LI()
    d1 = defaultdict(list)
    d2 = defaultdict(list)
    for _ in range(m):
        a, b, c = LI_()
        c += 1
        d1[a].append((b, c))
        d2[b].append((a, c))
    dist0 = dijkstra(0, d1)
    disti = dijkstra(0, d2)
    ans = 0
    for i in range(n):
        time = t - (dist0[i] + disti[i])
        ans = max(ans, time * A[i])
    print(ans)
    return

