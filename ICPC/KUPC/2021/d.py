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
    def check(a,b):
        if b & 1:
            return a & 1
        a = a % (b + 1)
        if a == b:
            return 2
        else:
            return a & 1
    n = II()
    ans = 1
    for _ in range(n):
        a,b = LI()
        print(check(a,b))
        ans ^= check(a,b)
    print(["Bob", "Alice", "Alice"][ans])



    # a -= b - 1
    # f = (int(math.log(a, b)) + 1) & 1

    # n = 10
    # m = 500
    # for i in range(2, n+1):
    #     print(i, " == start ==")
    #     dp = [0] * (m+1)
    #     for k in range(1, m+1):
    #         for xi in range(m+1):
    #             xi = pow(i, xi)
    #             if k - xi >= 0:
    #                 dp[k] |= not(dp[k - xi])
    #     x = 1
    #     # print(dp[0], end=" ")
    #     for mi in range(1, m+1):
    #         if math.log(mi, i) >= x:
    #             print()
    #             x += 1
    #         print(dp[mi], end=" ")
    #     print()
    #     print()

    return


#main
if __name__ == '__main__':
    solve()