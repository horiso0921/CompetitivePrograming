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
mod = 998244353
inf = 1e10

#solve
def solve():
    n,d = LI()
    ans = 0
    r = d - 1
    m =
    for i in range(n):
        tmp = 0
        if i >= :
            tmp += pow(2, d - i, mod)
        if r >= 0:
            tmp += pow(2, r, mod)
        

        if n + i - 2 >= d:
            if (i - 1) * 2 < d:
                tmp += pow(2, d - i, mod)
            else:
                tmp += pow(2, d - 1, mod)
                if d - i >= 0:
                    tmp -= pow(2, d - i, mod)
        
        print(tmp, n + i - 2 > d, i ,(i - 1) * 2 < d, d - i >= 0)
        tmp *= pow(2, i-1, mod)
        tmp %= mod
        ans += tmp
        ans %= mod
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()