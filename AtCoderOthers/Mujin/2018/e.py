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
inf = float("INF")

#solve
def solve():
    n, m, k = LI()
    d = S()
    s = SR(n)
    UDLR = ["U", "D", "L", "R"]
    mv = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    move = [[] for i in range(4)]
    for i in range(k):
        move[UDLR.index(d[i])].append(i)
    OK = []
    for i in range(4):
        mvi = move[i]
        if len(mvi):
            mvi.append(mvi[0] + k)
            OK.append(i)
    for i in range(n):
        for j in range(m):
            if s[i][j] == "S":
                start = (i, j)
            if s[i][j] == "G":
                goal = (i, j)
    q = [(0, start)]
    dist = [[inf] * m for i in range(n)]
    dist[start[0]][start[1]] = 0
    c = [[False] * m for i in range(n)]
    movei = [[inf] * (2 * k) for i in range(4)]
    for i in range(4):
        for mi in move[i]:
            movei[i][mi] = mi
        for j in range(2 * k - 2, -1, -1):
            movei[i][j] = min(movei[i][j], movei[i][j + 1])
    while q:
        time, yx = heappop(q)
        y, x = yx
        if c[y][x]:
            continue
        c[y][x] = 1
        for i in OK:
            my, mx = mv[i]
            my += y
            mx += x
            if 0 <= my < n and 0 <= mx < m and s[my][mx] != "#":
                move_time = movei[i][time % k] - time % k
                move_time += time + 1
                if dist[my][mx] > move_time:
                    dist[my][mx] = move_time
                    heappush(q, (move_time, (my, mx)))
    print(dist[goal[0]][goal[1]] if dist[goal[0]][goal[1]] != inf else -1)
    return


#main
if __name__ == '__main__':
    solve()
