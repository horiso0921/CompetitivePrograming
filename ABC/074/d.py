
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
    n = II()
    edg = LIR(n)

    ans = 0
    for i in range(n):
        for k in range(i + 1, n):
            ans += edg[i][k]

    for x in range(n):
        for y in range(x + 1, n):
            for k in range(n):
                if x == k or y == k:
                    continue
                if edg[x][y] > edg[x][k] + edg[k][y]:
                    print(-1)
                    return
                if edg[x][y] == edg[x][k] + edg[k][y]:
                    ans -= edg[x][y]
                    break

    print(ans)

    return

