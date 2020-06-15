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
inf = float('INF')

#solve
def solve():
    n, q = LI()
    edg = defaultdict(set)
    redg = defaultdict(set)
    for i in range(q):
        s = LS()
        if s[0] == "1":
            a, b = s[1], s[2]
            edg[a].add(b)
            redg[b].add(a)
        elif s[0] == "2":
            for re in list(redg[s[1]]):
                edg[s[1]].add(re)
                redg[re].add(s[1])
        elif s[0] == "3":
            x = edg[s[1]]
            for e in list(x):
                for i in list(edg[e]):
                    if i == s[1]:
                        continue
                    edg[s[1]].add(i)
                    redg[i].add(s[1])
    for i in range(n):
        for j in range(n):
            print("Y" if str(j + 1) in edg[str(i + 1)] else "N", end="")
        print()
    return


#main
if __name__ == '__main__':
    solve()
