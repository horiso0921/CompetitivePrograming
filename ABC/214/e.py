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
inf = 1e10

#solve
def solve():
    t = II()
    for _ in range(t):
        n = II()
        lr = LIR(n)
        lr.sort()
        i = 0
        j = 0
        can = []
        while i < inf and j < n:
            if can:
                x = heappop(can)
                if i > x:
                    print("No")
                    break
                i += 1
                while j < n and lr[j][0] <= i:
                    heappush(can, lr[j][1])
                    j += 1
            else:
                if lr[j][0] > i:
                    i = lr[j][0]
                    continue
                while j < n and  lr[j][0] <= i:
                    heappush(can, lr[j][1])
                    j += 1

        else:
            while can:
                x = heappop(can)
                if i > x:
                    print("No")
                    break
                i += 1
            else:
                print("Yes")
    return


#main
if __name__ == '__main__':
    solve()