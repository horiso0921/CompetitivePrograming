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
inf = float('INF')

#solve
def solve():
    n = II()
    c = LI()
    q = II()
    minodd = min(c[::2])
    minall = min(c)
    sumodd = 0
    sumall = 0
    ans = 0
    for _ in range(q):
        s = LS()
        if s[0] == "1":
            x, a = map(int, s[1:])
            x -= 1
            if x & 1:
                if c[x] - sumall >= a:
                    c[x] -= a
                    ans += a
                    minall = min(minall, c[x] - sumall)
            else:
                if c[x] - sumall - sumodd >= a:
                    c[x] -= a
                    ans += a
                    minall = min(minall, c[x] - sumodd - sumall)
                    minodd = min(minodd, c[x] - sumodd - sumall)
        else:
            a = int(s[1])
            if s[0] == "2":
                if minodd >= a:
                    ans += a * ((n + 1) // 2)
                    minall = min(minall, minodd - a)
                    minodd = minodd - a
                    sumodd += a
            else:
                if minall >= a:
                    ans += a * n
                    minall -= a
                    minodd -= a
                    sumall += a
    print(ans)

    return


#main
if __name__ == '__main__':
    solve()
