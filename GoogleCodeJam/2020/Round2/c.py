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
    t = II()
    c = [0]
    warp = [-1]
    tmp = 0
    def dfs(i, node, di, x):
        tmp += 1
        f = 0
        for j in range(n):
            if i & 1:
                if warp[j] == -1:
                    warp[j] = node
                    warp[node] = i
                    c[j] |= 2
                    c[node] |= 1
                    dfs(i + 1, j, di, x + 1)
                    warp[j] = -1
                    c[j] ^= 2
                    c[node] ^= 1
                    warp[node] = -1
            else:
                if warp[j] == -1:
                    x, y = xy[node]
                    xj, yj = xy[j]
                    if di[0]*(yj - y) == (xj - x) * di[1]:
                        warp[j] = -inf
                        dfs(i, j, di, x + 1)
                        warp[j] = node
                        warp[node] = j
                        c[j] |= 1
                        c[node] |= 2
                        dfs(i + 1, j, di, x + 1)
                        warp[j] = -1
                        warp[node] = -1
                        c[j] ^= 2
                        c[node] ^= 1
                elif warp[j] != -inf:
                    if not f:
                        x, y = xy[node]
                        xj, yj = xy[j]
                        if di[0]*(yj - y) == (xj - x) * di[1]:
                            if c[j] & 1:
                                tmp = max(tmp, x)
                                f = (xj, yj)
                            else:
                                c[j] |= 1
                                next = warp[j]
                                c[next] |= 2
                                dfs(i, next, di, x)
                    else:
                        x, y = xy[node]
                        xj, yj = xy[j]
                        if di[0]*(yj - y) == (xj - x) * di[1]:
                            xi, yi = f
                            if (xi - x) ** 2 + (yi - y) ** 2 < (yj - y) ** 2 + (xj - x) ** 2:
                                continue
                            else:
                                warp[j] = -inf
                                dfs(i, j, di, x + 1)
                                warp[j] = node
                                warp[node] = j
                                c[j] |= 1
                                c[node] |= 2
                                dfs(i + 1, j, di, x + 1)
                                warp[j] = -1
                                warp[node] = -1
                                c[j] ^= 2
                                c[node] ^= 1
        tmp = max(tmp, x)




    ans = [None] * t
    for i in range(t):
        n = II()
        xy = LIR(n)
        tmp = min(2, n)
        for i1 in range(n):
            for i2 in range(n):
                if i1 != i2:
                    c = [0] * n
                    warp = [-1] * n
                    c[i1] = 1
                    c[i2] = 2
                    warp[i1] = i2
                    warp[i2] = i1
                    for i3 in range(n):
                        if i1 != i3 and i2 != i3:
                            di = (xy[i2][0] - xy[i3][0], xy[i2][1] - xy[i3][1])
                            dfs(1, i3, di, 3)
        ans[i] = tmp

    for i in range(t):
        print("Case #{}: {}".format(i + 1, ans[i]))
    return


#main
if __name__ == '__main__':
    solve()
