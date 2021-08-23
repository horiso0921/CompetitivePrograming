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

import datetime
#solve
def solve():
    n = II()
    d_target = datetime.date(2012, 1, 1)
    holiday = set([i for i in range(365) if i % 7 in [0, 6]])
    for _ in range(n):
        m, d = map(int, input().split("/"))
        d_ = datetime.date(2012, m, d)
        td = (d_ - d_target).days
        while td in holiday:
            td += 1
        holiday.add(td)
    d = defaultdict(int)
    b = -1
    ans = 0
    tmp = 0
    for i in sorted(holiday):
        if i >= 366:
            break
        if i == b + 1:
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 1
        b = i
    print(max(ans, tmp))


    return


#main
if __name__ == '__main__':
    solve()
