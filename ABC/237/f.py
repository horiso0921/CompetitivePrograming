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
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 998244353
inf = 1e10

#solve
def solve():
    n,m = LI()
    dp = defaultdict(int)
    dp[(11,11,11)] = 1
    for i in range(n):
        ndp = defaultdict(int)
        for key, value in dp.items():
            lkey = list(key)
            for i in range(1, m+1):
                for j in range(3):
                    if key[j] >= i:
                        break
                else:
                    continue
                lkey[j] = i
                ndp[tuple(lkey)] += value
                ndp[tuple(lkey)] %= mod

        dp = ndp
    ans = 0
    for k,v in dp.items():
        if k[-1] != 11:
            ans += v
            ans %= mod
    print(ans)
                    
                        
            
    return


#main
if __name__ == '__main__':
    solve()