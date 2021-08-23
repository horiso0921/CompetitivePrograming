
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
    n, m, R = LI()
    r = LI()
    edg = [[0 if i == k else inf for k in range(n)] for i in range(n)]
    for _ in range(m):
        a, b, c = LI_()
        edg[a][b] = c + 1
        edg[b][a] = c + 1
    for k in range(n):
        for a in range(n):
            for b in range(n):
                edg[a][b] = min(edg[a][b], edg[a][k] + edg[k][b])
    ans = inf
    fullserch = itertools.permutations(range(R), R)
    for fulls in fullserch:
        b = 0
        for i in range(R - 1):
            b += edg[r[fulls[i]] - 1][r[fulls[i + 1]] - 1]
        ans = min(ans, b)
    print(ans)
    return

