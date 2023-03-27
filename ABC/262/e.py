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
    edg = [[] for _ in range(n)]
    for u,v in LIR_(m):
        edg[u].append(v)
        edg[v].append(u)
    q = []
    odd_odd = 0
    odd_even = 0
    even_even = 0
    for e in edg:
        for ei in e:
            if len(e) & 1:
                if len(edg[ei]) & 1:
                    odd_odd 
        if len(e) & 1:
            odd += 1
        else:
            even += 1
    q.append((1, 0, odd, even))
    ans = 0
    for cnt, done, odd, even in q:
        if done == k:
            ans += cnt
            ans %= mod
        q.append(cnt + odd, done + 1, odd)
        
    return


#main
if __name__ == '__main__':
    solve()