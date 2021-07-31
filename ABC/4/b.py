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
    a1 = list(map(str, input().split()))
    a2 = list(map(str, input().split()))
    a3 = list(map(str, input().split()))
    a4 = list(map(str, input().split()))

    ans = []
    ans.append(a1)
    ans.append(a2)
    ans.append(a3)
    ans.append(a4)

    for i in range(3,-1,-1):
        for k in range(3,-1,-1):
            print(ans[i][k], end=" ")
        print()
    return


#main
if __name__ == '__main__':
    solve()
