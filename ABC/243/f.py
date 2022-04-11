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
    n,m,k = LI()
    w = IR(n)
    ans = 0
    fact = [i for i in range(51)]
    fact[0] = 1
    for i in range(50):
        fact[i+1] *= fact[i]
        fact[i+1] %= mod
    kcm = fact[k] * pow(fact[m] * fact[k-m], mod-2, mod) % mod
    print(kcm)
    if k < m:
        print(0)
        return
    for mask1 in range(1<<n//2):
        f1 = 1
        s1 = 0
        cnt = 0
        for j in range(n//2):
            if mask1 & 1 << j:
                wj = w[j]
                f1 *= wj
                s1 += wj
                cnt += 1
        for mask2 in range(1<<(n-n//2)):
            f2 = 1
            s2 = 0
            tmp_cnt = 0
            for j in range(n-n//2):
                if mask2 & 1 << j:
                    wj = w[n//2 + j]
                    f2 *= wj
                    s2 += wj
                    tmp_cnt += 1
            if tmp_cnt + cnt == m:
                tmp = f1 * f2 % mod
                s = s1 + s2
                tmp *= pow(s, k-m, mod)
                print(tmp,mask1, mask2, s, f1 , f2)
                tmp %= mod
                ans += tmp
                ans %= mod
    print(ans * pow(pow(sum(w), k, mod), mod-2, mod) % mod)                
                
            
            
    
    return


#main
if __name__ == '__main__':
    solve()