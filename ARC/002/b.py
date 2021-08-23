
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
def B():
    y, m, d = map(int, input().rstrip().split("/"))
    t = [4, 6, 9, 11]
    def f(y, m, d):
        y /= m
        y /= d
        return not y.is_integer()

    while f(y, m, d):
        d += 1
        if m in t:
            if d == 31:
                d = 1
                m += 1
        else:
            if m == 2:
                if y % 400 == 0 or y % 100 != 0 and y % 4 == 0:
                    if d == 30:
                        d = 1
                        m += 1
                else:
                    if d == 29:
                        d = 1
                        m += 1
            else:
                if d == 32:
                    d = 1
                    m += 1
                    if m >= 13:
                        m = 1
                        y += 1
    print("{:04d}/{:02d}/{:02d}".format(y, m, d))
    return

