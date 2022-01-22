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
N = 5010
fact = [i for i in range(N)]
fact[0] = 1
for i in range(N-1):
    fact[i+1] *= fact[i]
    fact[i+1] %= mod
invfact = [i for i in range(N)]
invfact[N-1] = pow(fact[N-1], mod-2, mod)

for i in range(N-2, -1, -1):
    invfact[i] = invfact[i+1] * (i+1)
    invfact[i] %= mod

def combination_mod(n, k):
    """ power_funcを用いて(nCk) mod p を求める """ 
    """ nCk = n!/((n-k)!k!)を使用 """
    if n < 0 or k < 0 or n < k: return 0
    if n == 0 or k == 0: return 1
    a = fact[n]
    b = invfact[k] 
    c = invfact[n - k]
    return ((a * b) % mod) * c % mod

from copy import deepcopy

#solve
def solve():
    s = S()
    d = defaultdict(int)
    for si in s:
        d[si] += 1
    ans = [0] * 5010
    ans[0] = 1
    for v in d.values():
        na = [i for i in ans]
        for k, vi in enumerate(ans):
            if vi == 0: continue
            for v_ in range(1, v+1):
                na[k + v_] += (vi * combination_mod(k+v_, v_)) % mod
                na[k + v_] %= mod
        ans = na
    a = 0
    for v in ans:
        a += v
        a %= mod
    print(a-1)
    return


#main
if __name__ == '__main__':
    solve()