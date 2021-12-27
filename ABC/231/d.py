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
    for i in range(m):
        a,b = LI_()
        edg[a].append(b)
        edg[b].append(a)
    for i in range(n):
        if len(edg[i]) >= 3:
            print("No")
            return
    c = [0] * n
    for i in range(n):
        if c[i]: continue 
        q = [(i,-1)]
        c[i] = 1
        while q:
            p,pre = q.pop()
            for e in edg[p]:
                if e != pre:
                    if c[e]:
                        print("No")
                        return
                    c[e] = 1
                    q.append((e, p))
    print("Yes")
    
    return


#main
if __name__ == '__main__':
    solve()