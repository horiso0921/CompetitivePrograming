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
inf = float("inf")

#solve
def solve():
    n,k = LI()
    a = LI()
    sa = sorted(set(a))
    da = {}
    for i in range(len(sa)):
        da[sa[i]] = i
    lis1 = [inf] * len(sa)
    for i,ai in enumerate(a[k:], start=k):
        lis1[da[ai]] = min(lis1[da[ai]], i)
    for i in range(len(sa)-1, 0,-1):
        lis1[i-1] = min(lis1[i], lis1[i-1])
    lis1 = lis1[1:] + [inf]
    ans = inf
    for i in range(k):
        ans = min(ans, lis1[da[a[i]]] - i)
    if ans == inf:
        print(-1)
    else:
        print(ans)
    return


#main
if __name__ == '__main__':
    solve()