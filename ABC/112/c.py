
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
    n = II()
    xyh = LIR(n)
    xyh.sort(key = lambda x:x[2], reverse = True)
    x1, y1, h1 = xyh[0]
    del xyh[0]
    for x in range(101):
        for y in range(101):
            h = abs(x - x1) + abs(y - y1) + h1
            flg = True
            for xn, yn, hn in xyh:
                if max(h - abs(x - xn) - abs(y - yn), 0) == hn:
                    continue
                flg = False
                break
            if flg:
                print(x, y, h)
                return 
    return

