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
def solve(h,w):
    a = SR(h)
    dp = [[[0] * (1 << w+1) for i in range(w)] for j in range(h+1)]
    dp[0][0][0] = 1

    for i in range(h):
        for j in range(w):
            for used in range(1 << w + 1):
                now = dp[i][j][used]
                if used & 1 or a[i][j] == "#":
                    next = used >> 1
                    if j + 1 < w:
                        dp[i][j+1][next] += now
                    else:
                        dp[i+1][0][next] += now
                    
                    # .a
                    # aa
                    if j + 1 < w and i + 1 < h:
                        if a[i+1][j+1] == "#" or a[i+1][j] == "#" or a[i][j+1] == "#":
                            continue
                        if not (used >> 1 & 1) and not (used >> w & 1):
                            next = used | 2 | (1 << w) | (1 << (w+1))
                            next = next >> 1
                            dp[i][j+1][next] += now

                else:
                    # aa
                    # .a
                    if j + 1 < w and not (used >> 1 & 1) and a[i][j+1] != "#":
                        if i + 1 < h and a[i+1][j+1] != "#":
                            next = used | 2 | (1 << (w + 1))
                            next = next >> 1
                            dp[i][j+1][next] += now

                    # a.
                    # aa
                    if i + 1 < h and not (used >> w & 1) and a[i+1][j] != "#":
                        if j + 1 < w and a[i+1][j+1] != "#":
                            next = used | (1 << w) | (1 << (w + 1))
                            next = next >> 1
                            dp[i][j+1][next] += now
                    
                    # aa
                    # a.
                    if j + 1 < w and not (used & 1 << 1) and a[i][j+1] != "#":
                        if i + 1 < h and not (used >> w & 1) and a[i+1][j] != "#":
                            next = used | (1 << w) | 2
                            next = next >> 1
                            dp[i][j+1][next] += now

    print(dp[h][0][0])


                
    return


#main
if __name__ == '__main__':
    while 1:    
        h,w = LI()
        if h == w == 0: break
        solve(h,w)