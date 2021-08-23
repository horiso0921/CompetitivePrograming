
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
def C():
    def primes2(n):
        """https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188"""
        """ Returns  a list of primes < n """
        sieve = [True] * (n//2)
        for i in range(3,int(n**0.5)+1,2):
            if sieve[i//2]:
                sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
        return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]
    n = II()
    prime = primes2(n+1)
    d = []
    for i in prime:
        b = n
        f = 0
        while b:
            b = b // i
            f += b
        d.append(f%mod)
    ans = 1
    for i in d:
        ans *= (i + 1)
        ans %= mod
    print(ans)
    return

