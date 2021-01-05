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

#solve
def solve():
    n = II()
    edg = [[] for i in range(n)]
    ab = LIR_(n-1)
    for a,b in ab:
        edg[a].append(b)
        edg[b].append(a)
    rank = [0 for i in range(n)]
    check = set([0])
    tmp = [0]
    for p in tmp:
        for e in edg[p]:
            if e in check: continue
            check.add(e)
            tmp.append(e)
            rank[e] = rank[p] + 1

    ans = [0] * n
    ans1 = 0
    
    for _ in range(II()):
        t,e,x = LI()
        e -= 1
        a,b = ab[e]
        if t == 2: a,b = b,a
        if rank[a] > rank[b]:
            ans[a] += x
        else:
            ans[b] -= x
            ans1 += x
    check = set([0])
    tmp = [0]
    for p in tmp:
        for e in edg[p]:
            if e in check: continue
            check.add(e)
            tmp.append(e)
            ans[e] += ans[p]
    for i in range(n):
        print(ans1 + ans[i])
    return


#main
if __name__ == '__main__':
    solve()