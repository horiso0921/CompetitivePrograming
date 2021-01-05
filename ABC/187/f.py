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
    n,m = LI()
    edg = [[] for i in range(n)]
    ab = LIR_(m)
    for a,b in ab:
        edg[a].append(b) 
        edg[b].append(a) 
    dp = [None] * (1 << n)
    bit = [1 << i for i in range(n)]
    for i in range(n):
        dp[bit[i]] = 1
    def f(mask):
        if dp[mask] != None:
            return dp[mask]
        tmp = []
        tmp1 = []
        for i in range(n):
            if mask & bit[i]: 
                tmp1.append(i)
            else:
                tmp.append(i)
        if tmp1:
            for i in tmp1:
                tm = 0
                for e in edg[i]:
                    if mask & bit[e]:
                        tm += 1
                if tm + 1 < len(tmp1):
                    break
            else:
                dp[mask] = 1
                return 1
        res = inf
        for tmpmask in range(1, (1 << len(tmp)) - 1):
            tmask1 = 0
            tmask2 = 0
            for j in range(len(tmp)):
                if tmpmask & bit[j]:
                    tmask1 |= bit[tmp[j]]
                else:
                    tmask2 |= bit[tmp[j]]

            res = min(res, f(tmask1)+f(tmask2))
        dp[mask] = res
        return res
    print(f(0))
    return


#main
if __name__ == '__main__':
    solve()