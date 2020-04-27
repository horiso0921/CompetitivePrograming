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
    round = lambda x: (x * 2 + 1) // 2
    deg, dis = LI()
    ans = ["", 0]
    ansdeg = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","N"]
    deg *= 10
    dis /= 60
    dis = round(dis * 10)
    dis /= 10
    ans[0] = ansdeg[int(round(deg / 2250))]
    if dis <= 0.2:
        x = 0
    elif 0.3 <= dis and dis <= 1.5:
        x = 1
    elif 1.6 <= dis and dis <= 3.3:
        x = 2
    elif 3.4 <= dis and dis <= 5.4:
        x = 3
    elif 5.4 <= dis and dis <= 7.9:
        x = 4
    elif 8.0 <= dis and dis <= 10.7:
        x = 5
    elif 10.8 <= dis and dis <= 13.8:
        x = 6
    elif 13.9 <= dis and dis <= 17.1:
        x = 7
    elif 17.2 <= dis and dis <= 20.7:
        x = 8
    elif 20.8 <= dis and dis <= 24.4:
        x = 9
    elif 24.5 <= dis and dis <= 28.4:
        x = 10
    elif 28.5 <= dis and dis <= 32.6:
        x = 11
    else:
        x = 12
    ans[1] = x
    if x == 0:
        ans[0] = "C"
    print('{0[0]} {0[1]}'.format(ans))
    return


#main
if __name__ == '__main__':
    solve()
