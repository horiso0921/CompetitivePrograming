#!usr/bin/env python3
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
    n, s, t = LI()
    w = II()
    ans = 0
    for _ in range(n - 1):
        if s <= w <= t:
            ans += 1
        a = II()
        w += a
    if s <= w <= t:
        ans += 1
    #    print(w)
    print(ans) 

    return

#B
def B():
    n = II()
    a = IR(n)
    b = set(a)
    print(len(a)-len(b))        

    
    return

#C
def C():
    n, m = LI()
    vedg = defaultdict(lambda: inf)
    edge = [[] for i in range(n)]
    for _ in range(m):
        u, v, l = LI_()
        l += 1
        vedg[(u, v)] = l
        vedg[(v, u)] = l
        edge[v].append(u)
        edge[u].append(v)
    if len(edge[0]) < 2:
        print(-1)
        return
    ans = inf

    #ワーシャルフロイド
    field = [[None for __ in range(n)] for _ in range(n)]
    for u in range(1,n):
        for v in range(1,n):
            field[u][v] = vedg[(u,v)]

    for k in range(1,n):
        for i in range(1,n):
            for j in range(1,n):
                if field[i][j] > field[i][k] + field[k][j]:
                    field[i][j] = field[i][k] + field[k][j]

    for i in edge[0]:
        for k in edge[0]:
            if i == k:
                continue
            ans = min(ans, field[k][i] + vedg[(i, 0)] + vedg[(0, k)])
    if ans == inf:
        print(-1)
    else:
        print(ans)
    return

#D
def D():
    n = II()
    a = LIR(n)
    centera = [0, 0]
    for x,y in a:
        centera[0] += x
        centera[1] += y
    centera[0] /= n
    centera[1] /= n
    longesta = 0
    for x, y in a:
        longesta = max(longesta, (centera[0] - x)** 2 + (centera[1] - y)** 2)
    b = LIR(n)
    centerb = [0, 0]
    for x,y in b:
        centerb[0] += x
        centerb[1] += y
    centerb[0] /= n
    centerb[1] /= n
    longestb = 0
    for x, y in b:
        longestb = max(longestb, (centerb[0] - x)** 2 + (centerb[1] - y)** 2)
    print(math.sqrt(longestb)/math.sqrt(longesta))
    return

#Solve
if __name__ == '__main__':
    D()
