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
def LS(): return input().split()
def S(): return input().rstrip()
def IR(n): return [II() for _ in range(n)]
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
    first, last = LS()
    n = II()
    s = [first] + SR(n) + [last]
    lens = len(s[0])
    if first == last:
        print(0)
        print(first)
        print(first)
        return
    edg = [[] for i in range(n + 2)]
    for i in range(n + 2):
        for j in range(i + 1, n + 2):
            tmp = 0
            for k in range(lens):
                tmp += s[i][k] != s[j][k]
            if tmp == 1:
                edg[i].append(j)
                edg[j].append(i)
    revdist = [inf] * (n + 2)
    q = [(0, n + 1)]
    revdist[-1] = 0
    while q:
        score, i = heappop(q)
        for e in edg[i]:
            if revdist[e] > score + 1:
                revdist[e] = score + 1
                heappush(q, (score + 1, e))
    if revdist[0] == inf:
        print(-1)
        return
    print(revdist[0]-1)
    q = [0]
    while q:
        p = q.pop()
        print(s[p])
        for e in edg[p]:
            if revdist[p] - 1 == revdist[e]:
                
                q.append(e)
                break
    return


#main
if __name__ == '__main__':
    solve()
