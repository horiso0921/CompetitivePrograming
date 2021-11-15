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
    n = II()
    q = II()
    row_col = [[i for i in range(n)], [i for i in range(n)]]
    c = 0
    for _ in range(q):
        q = LI_()
        if q[0] == 0:
            a, b = q[1:]
            row_col[c][a], row_col[c][b] = row_col[c][b], row_col[c][a]
        elif q[0] == 1:
            a, b = q[1:]
            row_col[c ^ 1][a], row_col[c ^ 1][b] = row_col[c ^ 1][b], row_col[c ^ 1][a]
        elif q[0] == 2:
            c ^= 1
        else:
            a, b = q[1:]
            if c:
                print(row_col[1][a] + row_col[0][b] * n)
            else:
                print(row_col[0][a] * n + row_col[1][b])
        # print(row_col)
    return


#main
if __name__ == '__main__':
    solve()
