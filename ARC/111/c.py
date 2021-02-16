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
def LFR(n): return [LF() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    n = II()
    a = LI()
    A = [(a[i], i) for i in range(n)]
    A.sort()
    b = LI()
    p = LI_()
    baggage = [0] * n
    for i in range(n):
        baggage[p[i]] = i
    ans = []
    for ai, i in A:
        if baggage[i] == i:
            continue
        if b[p[i]] >= ai:
            print(-1)
            return
        h = baggage[i]
        if b[p[h]] >= a[h]:
            print(-1)
            return
        p[h], p[i] = p[i], p[h]
        baggage[p[i]] = i
        baggage[p[h]] = h
        ans.append((i+1,h+1))
    print(len(ans))
    for ai in ans:
        print(*ai)
    return


#main
if __name__ == '__main__':
    solve()