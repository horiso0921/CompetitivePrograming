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
mod = 998244353
inf = 1e10
fact = [i for i in range(2*10**5+1)]
for i in range(2*10**5):
    fact[i+1] *= fact[i]
    fact[i+1] %= mod

def combination_mod(n, k, mod):
    """ power_funcを用いて(nCk) mod p を求める """
    """ nCk = n!/((n-k)!k!)を使用 """
    from math import factorial
    if n < 0 or k < 0 or n < k:
        return 0
    if n == 0 or k == 0:
        return 1
    a = fact[n] % mod
    b = fact[k] % mod
    c = fact[n - k] % mod
    return (a * pow(b, mod - 2, mod) * pow(c, mod - 2, mod)) % mod
#solve
def solve():
    n,m,k = LI()
    ans = 0
    if n == 1:
        if m == 1:
            print(k)
        else:
            for i in range(1, k+1):
                ans += pow(k-i+1, m, mod)-pow(k-i,m,mod)
            print(ans%mod)
        return
    if m == 1:
        ans += 1
        for i in range(2, k+1):
            ans += pow(i,n,mod) - pow(i-1, n,mod)
        print(ans %mod)
        return
    for i in range(1, k+1):
        ans += (pow(i, n, mod) - pow(i-1, n,mod)) * pow(k-i+1, m, mod)
        ans %= mod
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
