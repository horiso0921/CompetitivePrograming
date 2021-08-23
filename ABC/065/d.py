
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
# 最小全域木の求め方のうちクルスカルのアルゴリズムをえた
# まぁムズイ
def D():
    def find(x):
        if x == par[x]:
            return x
        par[x] = find(par[x])
        return par[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y: return False
        par[x] = y
        return True
    n = II()
    par = [i for i in range(n)]
    xy = LIR(n)
    for i in range(n):
        xy[i].append(i)
    xy.sort(key=lambda x: x[0])
    edg = [None] * (2 * n - 2)
    a = 0
    for i in range(n-1):
        edg[i] = [xy[i + 1][0] - xy[i][0], xy[i][2], xy[i + 1][2]]
    xy.sort(key=lambda x: x[1])
    for i in range(n-1):
        edg[n + i - 1] = [xy[i + 1][1] - xy[i][1], xy[i][2], xy[i + 1][2]]
    ans = 0
    a = 0
    edg.sort(key=lambda x: x[0])
    for i in range(2 * n - 2):  
        value, p0, p1 = edg[i]
        if a == n - 1:
            break
        if unite(p0, p1):
            a += 1
            ans += value
    print(ans)
    return

