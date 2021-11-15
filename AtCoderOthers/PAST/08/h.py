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
inf = float("inf")

#solve
def solve():
    n,x = LI()
    edg = [[] for i in range(n)]
    for _ in range(n-1):
        a,b,c = LI_()
        c += 1
        edg[a].append((b,c))
        edg[b].append((a,c))
    for i in range(n):
        dist = [inf] * n
        q = deque([i])
        dist[i] = 0
        while q:
            p = q.pop()
            for e,c in edg[p]:
                if dist[e] > dist[p] + c:
                    dist[e] = dist[p] + c
                    if dist[p] + c > x:
                        continue
                    q.appendleft(e)
        for d in dist:
            if d == x:
                print("Yes")
                return
    print("No")
    return


#main
if __name__ == '__main__':
    solve()