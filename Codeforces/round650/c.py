#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
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
def IR(n):
    res = [None] * n
    for i in range(n):
        res[i] = II()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI()
    return res
def FR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR_(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI_()
    return res
def SR(n):
    res = [None] * n
    for i in range(n):
        res[i] = S()
    return res
def LSR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LS()
    return res
mod = 1000000007
inf = float('INF')

#solve
def solve():
    for _ in range(II()):
        n, k = LI()
        s = S()
        dp = [0] * (n+1)
        for i in range(n):
            if s[i] == "1":
                dp[i] = 1
        dp = list(itertools.accumulate(dp))
        i = 0
        ans = int(dp[k] == 0)
        while i < n - 1:
            if i + k + 1 >= n:
                break
            if dp[i] == dp[min(n - 1, i + 2 * k + 1)]:
                i = min(n - 1, i + k + 1)
                ans += 1
            else:
                i += 1
        print(ans)
    return


#main
if __name__ == '__main__':
    solve()
