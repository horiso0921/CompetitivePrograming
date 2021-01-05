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
def IR(n):
    res = [None] * n
    for i in range(n):
        res[i] = II()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI()
    return res
def FR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR_(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI_()
    return res
def SR(n):
    res = [None] * n
    for i in range(n):
        res[i] = S()
    return res
def LSR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LS()
    return res
mod = 1000000007
inf = float('INF')


#solve
def solve():
    t = II()
    for _ in range(t):
        n,m,k = LI()
        d = defaultdict(int)
        nu = defaultdict(int)
        edg = [[] for i in range(n)]
        for _ in range(m):
            u,v = LI_()
            edg[u].append(v)
            edg[v].append(u)
            d[(u,v)] = 1
            d[(v,u)] = 1
            nu[u] += 1
            nu[v] += 1
        print(nu)
        for i in range(n):
            if nu[i] < k:
                nu[i] = 0
                q = [i]
                while q:
                    p = q.pop()
                    for e in edg[p]:
                        if d[(e,p)]:
                            d[(e,p)] = 0 
                            d[(p,e)] = 0
                            nu[e] -= 1
                            if nu[e] < k:
                                q.append(e)
        print(nu)
        ans = []
        for i in range(n):
            if nu[i] >= k:
                ans.append(i+1)
        if len(ans) == k:
            print(2)
        else:
            print(1,len(ans))
        print(*ans)
        
    return


#main
if __name__ == '__main__':
    solve()
