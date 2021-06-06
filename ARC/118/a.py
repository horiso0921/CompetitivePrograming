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
    t,n = LI()
    tmp = set()
    tmp1 = []
    for i in range(1, 101):
        x = (100 + t) * i // 100
        if x in tmp: continue
        tmp.add(x)
        tmp1.append(i)
    xx = max(tmp) - len(tmp)
    nn = n // xx
    nnn = n % xx
    ans = nn * max(tmp)
    if nnn == 0:
        for i in range(max(tmp), 0, -1):
            if i not in tmp:
                print(ans - max(tmp) + i)
                return
    for i in range(1, max(tmp)):
        if nnn == 1 and i not in tmp:
            print(ans + i)
            return
        if i not in tmp:
            nnn -= 1        
    return


#main
if __name__ == '__main__':
    solve()