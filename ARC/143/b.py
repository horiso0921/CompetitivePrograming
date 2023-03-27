#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
from tabnanny import check
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

fact = [i for i in range(250001)]
fact[0] = 1
for i in range(250000):
    fact[i+1] *= fact[i]
    fact[i+1] %= mod
invfact = fact[:]
invfact[-1] = pow(invfact[-1], mod-2, mod)
for i in reversed(range(250000)):
    invfact[i] = invfact[i+1] * (i+1)
    invfact[i] %= mod
# print(invfact[-3] * fact[-3] % mod)
def nck(n,k):
    return fact[n] * invfact[k] * invfact[n-k] % mod

#solve
def solve():
    n = II()
    ans = fact[n ** 2]
    cand = n ** 2 - 2 * n + 1
    # print(cand)
    for i in range(n, n ** 2 - n + 2):
        tmp = nck(i-1, n-1) * n * fact[n]
        i_n = i - n
        tmp *= nck(cand, i_n) * fact[i_n]
        tmp %= mod
        tmp *= fact[n**2 - i]
        ans -= tmp
        ans %= mod
    print(ans)
    return

def check():
    n = II()
    full = [(i,j) for i in range(n) for j in range(n)]
    ans = 0
    d = defaultdict(int)
    for f in itertools.permutations(full, n**2):
        m = [[None] * n for _ in range(n)]
        for i,fi in enumerate(f):
            m[fi[0]][fi[1]] = i
        tmp = 0
        for i in range(n):
            for j in range(n):
                ttmp = 0
                mij = m[i][j]
                for i_ in range(n):
                    if mij > m[i_][j]:
                        ttmp = 1
                for j_ in range(n):
                    if mij < m[i][j_]:
                        ttmp = 1
                if ttmp:
                    continue
                tmp += 1
                d[m[i][j]] += 1
                break
            else:
                continue
            break
        if tmp:
            continue
            
        ans += 1
    print(ans)
    print(d)


#main
if __name__ == '__main__':
    # check()
    solve()