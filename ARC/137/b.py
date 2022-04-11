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
    n = II()
    a = [-1 if i else 1 for i in LI()]
    a = list(itertools.accumulate([0]+a))
    ansu = 0
    ansd = 0
    tmpu = 0
    tmpd = 0
    for ai in a:
        ansu = max(ansu, ai-tmpd)
        ansd = max(ansd, tmpu-ai)
        tmpu = max(tmpu, ai)
        tmpd = min(tmpd, ai)
        # print(tmpu, tmpd)
        
    print(ansu + ansd + 1)

    return


#main
if __name__ == '__main__':
    solve()