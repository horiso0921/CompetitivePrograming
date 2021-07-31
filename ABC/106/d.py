
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
# 始点と終点を2次元座標に落とし込むことで解ける
# 難しい
def D():
    n, m, q = LI()
    c = [[0] * (n+1) for i in range(n+1)]
    for _ in range(m):
        l, r = LI()
        c[r][l] += 1
    for y in range(1, n + 1):
        cy = c[y]
        for x in range(1, n + 1):
            cy[x] += cy[x - 1]
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            c[y][x] += c[y - 1][x]
    for _ in range(q):
        p, q = LI()
        ans = c[q][q] - c[q][p - 1] - c[p - 1][q] + c[p - 1][p - 1]
        print(ans)
    return

