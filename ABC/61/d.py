
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
# ベルマンフォード
# 最大化は符号反転の最小化
# 負閉路の判定方法もまた新たな知見
def D():
    n, m = LI()
    abc = LIR_(m)
    for i in range(m):
        abc[i][2] = -abc[i][2] - 1
    dist = [inf] * n
    dist[0] = 0
    for _ in range(n - 1):
        for a, b, c in abc:
            dist[b] = min(dist[a] + c , dist[b])
    check = [False] * n
    for _ in range(n):
        for a, b, c in abc:
            if check[a]:
                check[b] = True
            if dist[b] > dist[a] + c:
                check[b] = True
                dist[b] = dist[a] + c
    if check[n - 1]:
        print("inf")
    else:
        print(-dist[n - 1])
    return

