#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
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
inf = 1e10

#solve
def solve():
    x = II()
    ans = []
    q = []
    for i in range(1, 10):
        for j in range(1, 10):
            q.append((i, j))
            q.append((i, -j))
        q.append((i, 0))
        ans.append(i)
    for i,j in q:
        ni = i % 10
        if 0 <= ni + j < 10:
            xi = i * 10 + ni + j
            if xi >= 111111111111111112:
                continue
            ans.append(xi)
            q.append((xi, j))
    ans.sort()
    print(ans[bisect_left(ans, x)])
    return


#main
if __name__ == '__main__':
    solve()