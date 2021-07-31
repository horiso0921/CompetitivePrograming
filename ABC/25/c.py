
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
def C():
    b = LIR(2)
    c = LIR(3)

    def clc_score(field):
        ansb1 = 0
        ansb2 = 0
        for i,bi in enumerate(b):
            for j, bij in enumerate(bi):
                if field[i][j] == field[i + 1][j]:
                    ansb1 += bij
                else:
                    ansb2 += bij
        for i, ci in enumerate(c):
            for j, cij in enumerate(ci):
                if field[i][j] == field[i][j + 1]:
                    ansb1 += cij
                else:
                    ansb2 += cij
        return ansb1 - ansb2

    cross = itertools.combinations(range(9), 4)
    d = defaultdict(int)
    score = 0

    for bi in b:
        score += sum(bi)
    for ci in c:
        score += sum(ci)

    for cr in cross:
        field = [[0] * 3 for _ in range(3)]
        for ci in cr:
            field[ci // 3][ci % 3] = 1
        d[cr] = clc_score(field)


    def game_dfs(check, tern, cross):

        if tern == 10:
            cross.sort()
            return d[tuple(cross)]

        if tern % 2:
            res = -inf
            for i in range(9):
                if check[i]:
                    check[i] = False
                    res = max(game_dfs(check, tern + 1, cross), res)
                    check[i] = True
            return res

        else:
            res = inf
            for i in range(9):
                if check[i]:
                    check[i] = False
                    res = min(game_dfs(check, tern + 1, cross+[i]), res)
                    check[i] = True
            return res

    x = game_dfs([True] * 9, 1, [])
    print((score + x) // 2)
    print((score - x) // 2)

    return

