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

class Mystr:
    def __init__(self, string: str) -> None:
        self.str = string
    def __eq__(self, o: object) -> bool:
        return self.str + o.str == o.str + self.str
    def __lt__(self, o: object) -> bool:
        return self.str + o.str < o.str + self.str
    def __str__(self) -> str:
        return self.str


#solve
def solve():
    n,k = LI()
    s = [Mystr(S()) for _ in range(n)]
    s.sort()
    
    dp = [chr(ord("a") + 27)] * (k+1)
    
    for i in range(n-1,-1,-1):
        ndp = dp[:]
        si = s[i]
        dp[0] = ""
        for ki in range(k):
            d = si.str + dp[ki]
            if d < ndp[ki+1]:
                ndp[ki+1] = d
        dp = ndp
    
    print(dp[-1])

#main
if __name__ == '__main__':
    solve()