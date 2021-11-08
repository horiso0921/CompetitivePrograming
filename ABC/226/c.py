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
mod = 1000000007
inf = 1e10

#solve
def solve():
    n = II()
    edg = [[] for i in range(n)]
    ans = 0
    s = [0] * n
    for i in range(n):
        t,k,*a = LI()
        s[i] = t
        for ai in a:
            edg[i].append(ai - 1)
    q = [n-1]
    ans += s[-1]
    c = [0] * n
    c[-1] = 1
    while q:
        i = heappop(q)
        for e in edg[i]:
            if c[e]: continue
            q.append(e)
            ans += s[e]
            c[e] = 1
    print(ans)           
    return


#main
if __name__ == '__main__':
    solve()