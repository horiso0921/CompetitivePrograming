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
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#solve
def solve():
    n, m = LI()
    a = SR(n)
    d = defaultdict(list)
    for i in range(n):
        for j in range(m):
            d[a[i][j]].append((i, j))
    edg = defaultdict(list)
    for i in range(1, 10):
        if len(d[str(i)]):
            continue
        print(-1)
        return
    for key, value in d.items():
        if key == "S":
            edg[value[0]] = d["1"]
        elif key == "G":
            pass
        elif key == "9":
            for v in value:
                edg[v] = d["G"]
        else:
            for v in value:
                edg[v] = d[str(int(key) + 1)]
    dist = defaultdict(lambda: inf)
    dist[d["S"][0]] = 0
    q = [(0, d["S"][0])]
    while q:
        score, p = heappop(q)
        px,py = p
        for e in edg[p]:
            ex, ey = e
            if dist[e] > score + abs(px - ex) + abs(py - ey):
                dist[e] = score + abs(px - ex) + abs(py - ey)
                heappush(q, (score + abs(px - ex) + abs(py - ey), e))

    print(dist[d["G"][0]])
    return


#main
if __name__ == '__main__':
    solve()
