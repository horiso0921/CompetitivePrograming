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
def IR_(n): return [II() - 1 for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#solve
def solve():
    n = II()
    P = IR_(n)
    edg = [[] for i in range(n)]
    for i in range(n):
        if P[i] == -2: continue
        edg[P[i]].append(i)
    Q = II()
    rank = [None] * n
    for i in range(n):
        if P[i] == -2: boss = i
    q = deque([boss])
    rank[boss] = 0
    while q:
        p = q.popleft()
        for e in edg[p]:
            rank[e] = rank[p] + 1
            q.append(e)
    per = [[-1] * n for i in range(n.bit_length())]
    for i in range(n):
        per[0][i] = P[i]
    for i in range(1, n.bit_length()):
        for j in range(n):
            if per[i - 1][j] == -1: continue
            per[i][j] = per[i - 1][per[i - 1][j]]
    for i in range(Q):
        a, b = LI_()
        if rank[a] <= rank[b]:
            print("No")
        else:
            diff = rank[a] - rank[b]
            i = 0
            while diff:
                if diff & 1:
                    a = per[i][a]
                i += 1
                diff >>= 1
            if a == b:
                print("Yes")
            else:
                print("No")
    return


#main
if __name__ == '__main__':
    solve()
