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
    n = II()
    ab = LIR(n)
    suv = [i for i in range(n)]
    while len(suv) > 1:
        tmp = []
        for i in range(0, len(suv) - 1, 2):
            j = suv[i + 1]
            i = suv[i]
            a1, b1 = ab[i]
            a2, b2 = ab[j]
            if (a1 + b2 - 1) // b2 > (a2 + b1 - 1) // b1:
                tmp.append(i)
            elif (a1 + b2 - 1) // b2 < (a2 + b1 - 1) // b1:
                tmp.append(j)
        if len(suv) & 1:
            tmp.append(suv[-1])
        suv = tmp[::1]
    if len(suv) == 0:
        print(-1)
        return
    win = suv[0]
    a1, b1 = ab[win]
    for i in range(n):
        if win == i:
            continue
        a2, b2 = ab[i]
        if (a1 + b2 - 1) // b2 > (a2 + b1 - 1) // b1:
            continue
        print(-1)
        return
    print(win + 1)
    return


#main
if __name__ == '__main__':
    solve()
