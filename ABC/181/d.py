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
inf = float("INF")

#solve
def solve():
    s = S()
    full = defaultdict(int)
    for si in s:
        full[si] += 1
    tmp = []
    l = len(s)
    if l >= 3:
        l = 3
    for i in range(10 ** (l - 1), 10 ** l):
        if "0" in str(i):
            continue
        if i % 8 == 0:
            tmp.append(str(i))
    for t in tmp:
        x = defaultdict(int)
        for ti in t:
            x[ti] += 1
        xx = 1
        for key, val in x.items():
            if full[key] < val:
                xx = 0
        if xx:
            print("Yes")
            return
    print("No")
        
        
    
    return
                
        


#main
if __name__ == '__main__':
    solve()
