#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    w, h = LI()
    a = w / 4
    b = h / 3
    if a == b:
        print("4:3")
    else:
        print("16:9")
    return

#B
def B():
    s = S()
    t = II()
    now = [0, 0]
    q = 0
    d = defaultdict(int)
    d["U"] = (0, 1)
    d["L"] = (-1, 0)
    d["R"] = (1, 0)
    d["D"] = (0, -1)
    for i in s:
        if i == "?":
            q += 1
            continue
        now = [now[0] + d[i][0], now[1] + d[i][1]]
    x,y = map(abs,now)
    if t == 1:
        print(y + x + q)
        return
    if x + y >= q:
        print(x + y - q)
        return
    q -= x + y
    print(q % 2)
    return

#C
def C():
    n, q = LI()
    lis = [0] * (n + 1)
    for _ in range(q):
        l, r = LI_()
        lis[l] ^= 1
        lis[r + 1] ^= 1
    for i in range(n):
        lis[i + 1] ^= lis[i]
    print("".join(map(str,lis[:-1])))
    return

# D
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

#Solve
if __name__ == '__main__':
    D()
