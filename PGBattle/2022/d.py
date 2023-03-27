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
    n = II()
    ab = LIR(n)

    ab_gold = 0
    for a,b in ab:
        ab_gold += a * 10 + b
    
    if ab_gold & 1:
        print(0)
        return
    
    ab_gold //= 2
    
    ab = [[a%mod, b%mod] for a,b in ab]
    
    comb_mod = [[1] * 11 for _ in range(11)]
    for n_ in range(1, 11):
        for k_ in range(1, n_):
            comb_mod[n_][k_] = math.factorial(n_) * pow(math.factorial(k_), mod-2, mod) * pow(math.factorial(n_-k_), mod-2, mod) % mod
 
    ua = defaultdict(int)
    ua[0] = 1
    for a,_ in ab[:n//2]:
        n_ua = defaultdict(int)
        for k,v in ua.items():
            for i in range(11):
                ai = a * i
                n_ua[k+ai] += v * comb_mod[10][i] 
                n_ua[k+ai] %= mod
        ua = n_ua
    
    da = defaultdict(int)
    da[0] = 1
    for a,_ in ab[n//2:]:
        n_da = defaultdict(int)
        for k,v in da.items():
            for i in range(11):
                ai = a * i
                n_da[k+ai] += v * comb_mod[10][i]
                n_da[k+ai] %= mod
        da = n_da

    udb = defaultdict(int)
    for mask in range(1 << n):
        tmp = 0
        for i in range(n):
            if mask & 1 << i:
               tmp += ab[i][1]
        udb[tmp] += 1
   
    da_udb = defaultdict(int)
    for dai, vdai in da.items():
        for udbi, vudbi in udb.items():
            t = dai + udbi
            if ab_gold < t: continue
            da_udb[t] += vdai * vudbi 
            da_udb[t] %= mod

    ans = 0
    for uai,vuai in ua.items():
        ans += da_udb[ab_gold - uai] * vuai 
        ans %= mod
    
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()