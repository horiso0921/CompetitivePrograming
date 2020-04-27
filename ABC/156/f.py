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
inf = 1e10

#solve
def solve():
    k, q = LI()
    d = LI()
    for _ in range(q):
        n, x, m = LI()
        x %= m
        tmp = 0
        l = 0
        for i in range(k):
            tmp += d[i]
            l += (d[i + 1] - d[i]) // m
        term = (n - 2) // k + 1
        r = tmp * term
        r1 = r
        for p in range(n % k):
            if r1 % m > (r1 + d[p]) % m:
                pass
        print(r // m - l * term)
    return


#main
if __name__ == '__main__':
    solve()
