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
    a = LI()
    t = []
    i = 0
    xx = []
    for mask in range(n):
        if i == m:
            xx.append(mask)
            continue
        if a[i] == mask:
            i += 1
        else:
            xx.append(mask)
    tt=[]
    for x in xx:
        y=x
        for k in t:
            if x^k<x:
                x^=k
        if x: 
            t.append(x)
            tt.append(y)
    ans = []
    ch = defaultdict(int)
    q = deque([0])
    ch[0] = 1
    if len(t) != n.bit_length()-1:
        print(-1)
        return
    while q:
        p = q.pop()
        for k in tt:
            if ch[p^k] == 0:
                q.appendleft(p^k)
                ans.append((p,p^k))
                ch[p^k] = 1
    for ai in ans:
        print(*ai)
    return


#main
if __name__ == '__main__':
    solve()