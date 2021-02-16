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

def e(n):
    ret = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            ret -= ret // i
            while n % i == 0:
                n //= i
        i += 1
    if n > 1: ret -= ret // n
    return ret

#solve
def solve():
    t = II()
    for _ in range(t):
        n,s,k = LI()
        x = math.gcd(n,k)
        ns = n - s
        if x != 1:
            if ns % x != 0:
                print(-1)
                continue
            ns //= x
            n //= x
            k //= x
        ans = pow(k, e(n) - 1, n) * ns 
        print(ans % n)
            
            
    return


#main
if __name__ == '__main__':
    solve()