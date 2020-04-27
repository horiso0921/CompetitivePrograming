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
def solve():
    n = II()
    t = IR(n)
    ans = inf
    for i in range(n + 1):
        tmp = inf
        for fi in itertools.permutations(range(n), i):
            l = []
            fi = list(fi)
            ti = 0
            for fii in fi:
                ti += t[fii]
            tk = 0
            for k in range(n):
                if not k in fi:
                    tk += t[k]
            tmp = min(tmp, max(tk, ti))
        ans = min(ans, tmp)
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
