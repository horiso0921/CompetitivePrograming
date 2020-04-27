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
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
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
    r, c = LI()
    x, y = LI()
    d, l = LI()
    def comb(n,k):
        """power_funcを用いて(nCk) mod p を求める"""
        from math import factorial
        p = mod
        if n<0 or k<0 or n<k: return 0
        if n==0 or k==0: return 1
        a=factorial(n) %p
        b=factorial(k) %p
        c=factorial(n-k) %p
        return (a*power_func(b,p-2)*power_func(c,p-2))%p
    def power_func(a,b):
        """a^b mod p を求める"""
        if b==0: return 1
        if b%2==0:
            d = power_func(a, b // 2)
            return d*d %mod
        if b%2==1:
            return (a*power_func(a,b-1))%mod
    ans = 0
    
    #全辺使用
    zenbu = comb(x * y, d + l) * comb(d + l, d)
    
    #1辺未使用
    hen1 = comb(x * (y - 1), d + l) * comb(d + l, d) * 2
    hen1 += comb((x - 1) * y, d + l) * comb(d + l, d) * 2
    
    #2辺未使用
    hen2 = comb(x * (y - 2), d + l) * comb(d + l, d)
    hen2 += comb((x - 2) * y, d + l) * comb(d + l, d)
    hen2 += comb((x - 1) * (y - 1), d + l) * comb(d + l, d) * 4
    
    #3辺未使用
    hen3 = comb((x - 1) * (y - 2), d + l) * comb(d + l, d) * 2
    hen3 += comb((x - 2) * (y - 1), d + l) * comb(d + l, d) * 2
    
    #4辺未使用
    hen4 = comb((x - 2) * (y - 2), d + l) * comb(d + l, d)
    
    ans = zenbu - hen1 + hen2 - hen3 + hen4
    
    if x * y == d + l:
        ans = comb(x * y, d)
    ans = ans * (r-x+1)*(c-y+1)
    print(ans%mod)
    return


#main
if __name__ == '__main__':
    solve()
