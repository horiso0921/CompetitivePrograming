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
    n, w, c = LI()
    lrp = LIR(n)
    lis = [w - c] * (2 * n + 1)
    lis[0] = 0
    i = 1
    for l, r, _ in lrp:
        lis[i] = l - c + 1
        lis[i + 1] = r
        i += 2
    lis = list(set(lis))
    lis.sort()
    d = defaultdict(int)
    i = 0
    for li in lis:
        if li > w - c: break
        if li >= 0:
            d[li] = i
            i += 1
    dp = [0] * (len(d.keys()) + 1)
    for l, r, p in lrp:
        dp[d[max(0, l - c + 1)]] += p
        if r <= w - c: dp[d[r]] -= p
    dp = list(itertools.accumulate(dp))
    print(min(dp))
    return


#main
if __name__ == '__main__':
    solve()
