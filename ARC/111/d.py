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
def LFR(n): return [LF() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    t = II()
    def f(mid):
        ab = (a + b * mid) % d
        if (a + b * mid) // d != (a + c * mid) // d:
            return False
        ac = (a + c * mid) % d
        if ab < ac:
            return True
        else:
            return False
    def g(mid):
        ab = (a + b * mid) % d
        ac = (a + c * mid) % d
        if (a + b * mid) // d + 1 != (a + c * mid) // d:
            return False
        if ab < ac:
            return True
        else:
            return False
    
    for i in range(t):
        a,b,c,d = LI()
        ans = 0
        ok = 0
        ng = 10 ** 8
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if f(mid):
                ok = mid
            else:
                ng = mid
        ans += ok
        ok = 10 ** 8
        ng = 0
        while ok- ng > 1:
            mid = (ok + ng) // 2
            if g(mid):
                ok = mid
            else:
                ng = mid
        
    return


#main
if __name__ == '__main__':
    solve()