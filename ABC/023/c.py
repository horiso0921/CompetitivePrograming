
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
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
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
def C():
    R, C, K = LI()
    n = II()
    rc = LIR_(n)
    fldr = [0 for _ in range(R)]
    fldc = [0 for _ in range(C)]
    for r, c in rc:
        fldr[r] += 1
        fldc[c] += 1
    fldcs = fldc[::1]
    fldcs.sort()
    fldrs = fldr[::1]
    fldrs.sort()
    ans = 0
    for k in range(K+1):
        ans += (bisect.bisect_right(fldcs, K - k) - bisect.bisect_left(fldcs, K - k)) * (bisect.bisect_right(fldrs, k) - bisect.bisect_left(fldrs, k))
    for r, c in rc:
        a = fldr[r] + fldc[c]
        if a == K:
            ans -= 1
        elif a == K + 1:
            ans += 1
    print(ans)
    return

