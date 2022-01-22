#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import re
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
    h,w,k = LI()
    a = LI()
    b = LI()
    if sum(a) % k != sum(b) % k:
        print(-1)
        return
    ans = 0
    wk = w * (k - 1) % k
    for ai in a:
        if ai > wk:
            ans += w * (k-1) - (wk + k - ai)
        else:
            ans += w * (k-1) - (wk - ai)
    tmp = 0
    hk = h * (k - 1) % k
    for ai in b:
        if ai > hk:
            tmp += h * (k-1) - (hk + k - ai)
        else:
            tmp += h * (k-1) - (hk - ai)
        # print(tmp)
    print(min(ans, tmp))
    return

    


#main
if __name__ == '__main__':
    solve()