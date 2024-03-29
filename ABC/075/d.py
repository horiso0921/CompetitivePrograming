
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
    n, k = LI()
    xy = LIR(n)
    fullserch = list(itertools.combinations(range(n), 2))
    ans = inf
    for a, b in fullserch:
        minx = min(xy[a][0], xy[b][0])
        maxx = max(xy[a][0], xy[b][0])
        for c, d in fullserch:
            miny = min(xy[c][1], xy[d][1])
            maxy = max(xy[c][1], xy[d][1])
            x = 0
            
            for i in range(n):
                if minx <= xy[i][0] <= maxx and miny <= xy[i][1] <= maxy:
                    x += 1

            if x >= k:
                ans = min(ans, (maxx - minx) * (maxy - miny))
    print(ans) 
    return

