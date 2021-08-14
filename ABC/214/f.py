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
    s = S()
    nex = [[-1]*26 for i in range(len(s))]
    dp = [0] * len(s)
    for i in range(len(s)-1, 0,-1):
        si = s[i]
        si = ord(si) - ord("a")
        for al in range(26):
            ne = nex[i][al]
            if al == si:
                ne = i
            nex[i-1][al] = ne
    dp[0] = 1
    for ai in range(26):
        j = nex[0][ai]
        if j != -1 and ord(s[0]) - ord("a") != ai:
            dp[j] = 1

    for i in range(len(s)):
        dpi = dp[i]
        for ai in range(26):
            al = nex[i][ai]
            if al == i+1: al = nex[i+1][ai]
            if al != -1: 
                dp[al] += dpi
                dp[al] %= mod

    print(sum(dp)%mod)



    
    return


#main
if __name__ == '__main__':
    solve()