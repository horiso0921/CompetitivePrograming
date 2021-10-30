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

inf = float("inf")

mod = 10**9 + 7
base = 2009
# RH前に、必要な長さの最大値分のpow-tableを計算しておく
pw = [1]*(20000 + 1)
v = 1
for i in range(20000):
    pw[i+1] = v = v * base % mod

p2 = [i ** 2 for i in range(20001)]

 
       
#solve
def solve(s):
    
    lens = len(s) // 2
    
    def rolling_hash(s):
        l = len(s)
        h = [0]*(l + 1)
        v = 0
        for i in range(l):
            h[i+1] = v = (v * base + ord(s[i])) % mod
        return h

    dp = [inf] * (lens+1)
    dp[0] = 0
    ls = s[:lens]
    rs = s[-lens:]
    lss = ls
    rss = rs
    ls = rolling_hash(ls)
    rs = rolling_hash(rs)

    for l in range(1, lens+1):
        score = dp[l-1]
        if score == inf:
            continue
        if lss[l-1] == rss[lens-l]:
            if dp[l] > score:
                dp[l] = score
        lls = ls[l-1]
        rrs = rs[lens-l+1]
        for r in range(l+1, lens+1):
            if dp[r] > score + p2[r - l + 1]:
                zen = (ls[r] - lls * pw[r-l+1]) % mod
                kou = (rrs - rs[lens-r] * pw[lens-l+1-lens+r]) % mod
                if zen == kou:
                    dp[r] = score + p2[r - l + 1]

    if dp[-1] == inf:
        print(-1)
    else:
        print(dp[-1],flush=True) 




    return


#main
if __name__ == '__main__':
    while 1:
        n = S()
        if n == "#": break
        solve(n)