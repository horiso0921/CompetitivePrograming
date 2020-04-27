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
    n, k = LI()
    dp = [-1] * (k + 1)
    dp[0] = 0
    num = ["1110111", "0010010", "1011101", "1011011",
            "0111010", "1101011", "1101111", "1010010",
            "1111111", "1111011"]
    pre = [[0] * (1 << 7) for i in range(10)]
    for i in range(10):
        for mask in range(1 << 7):
            for j in range(7):
                if mask & (1 << j):
                    if num[i][-j-1] == "0":
                        pre[i][mask] = -1
                        break
    for i in range(10):
        for mask in range(1 << 7):
            if pre[i][mask] != -1:
                for j in range(7):
                    if int(num[i][-j-1]) != (mask >> j) & 1:
                        pre[i][mask] += 1
    for _ in range(n):
        s = S()
        tmp = [1] * 10
        dp2 = [-1] * (k + 1)
        mask = 0
        for i in range(7):
            if s[-i - 1] == "1":
                mask |= 1 << i
        for i in range(9, -1, -1):
            if pre[i][mask] != -1:
                l = pre[i][mask]
                for m in range(k - l + 1):
                    x = dp[m] * 10 + i
                    if dp2[m + l] < x:
                        dp2[m + l] = x
        dp = [None] * (k + 1)
        f = 0
        for i in range(k + 1):
            if dp2[i] != -1:
                f = 1
            dp[i] = dp2[i]
        if f:
            continue
        print(-1)
        return
    print(dp2[k])
    return


#main
if __name__ == '__main__':
    solve()
