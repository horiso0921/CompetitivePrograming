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
    n,m = LI()
    edg = [[] for i in range(n)]
    for _ in range(m):
        a,b = LI_()
        edg[a].append(b)
        edg[b].append(a)
    for _ in range(II()):
        done = defaultdict(int)
        x,k = LI_()
        k += 1
        ans = x + 1
        q = [x]
        done[x] = 1
        for _ in range(k):
            nex = []
            for qi in q:
                for e in edg[qi]:
                    if done[e]:
                        continue
                    done[e] = 1
                    nex.append(e)
                    ans += e + 1
            q = nex
        print(ans)
    return


#main
if __name__ == '__main__':
    solve()