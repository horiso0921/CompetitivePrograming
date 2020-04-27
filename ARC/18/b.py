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
    xy = LIR(n)
    ans = 0
    for full in itertools.combinations(range(n),3):
        i,k,l = full
        x1, y1 = xy[i]
        x2, y2 = xy[k]
        x3, y3 = xy[l]
        area = abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3))
        ans +=  not area & 1 and area != 0
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
