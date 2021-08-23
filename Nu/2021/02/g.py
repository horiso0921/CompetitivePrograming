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
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    n,m = LI()
    edg = [[] for i in range(n)]
    vedg = defaultdict(int)
    dp = defaultdict(int)
    for _ in range(m):
        x,y = LI_()
        edg[x].append(y)
        vedg[y] += 1
    
    q = deque()

    for i in range(n):
        if vedg[i] == 0:
            q.append(i)
    
    while q:
        p = q.popleft()

        for e in edg[p]:
            dp[e] = max(dp[e], dp[p] + 1)
            vedg[e] -= 1
            if vedg[e] == 0:
                q.append(e)
            
    print(max(dp.values()))

    return


#main
if __name__ == '__main__':
    solve()