
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
def D():
    def dij(s):
        dist = [inf for i in range(n)]
        dist[s] = 0
        q = [[0, s]]
        while q:
            d, f = heappop(q)
            for t, cost in edg[f]:
                if d + cost < dist[t]:
                    dist[t] = d + cost
                    heappush(q, [dist[t], t])
        return dist
    n, m = LI()
    ans = defaultdict(int)
    edg = defaultdict(list)
    for _ in range(m):
        a, b, c = LI_()
        c += 1
        edg[a].append((b, c))
        edg[b].append((a, c))
        ans[(a, b)] = False
        ans[(b, a)] = False
    for i in range(n):
        dis = dij(i)
        q = deque()
        q.append(i)
        while q:
            f = q.popleft()
            for t, cost in edg[f]:
                if dis[t] - dis[f] == cost:
                    ans[(t, f)] = True
                    q.append(t)
    ans = list(ans.values())
    print(ans.count(False) // 2)
    return

