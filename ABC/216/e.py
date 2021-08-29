#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heapify, heappush, heappop
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
    n,k = LI()
    a = [-i for i in LI()]
    heapify(a)
    heappush(a, 0)
    pre = -heappop(a)
    ans = 0
    j = 1
    while a:
        p = -heappop(a)
        diff = pre - p
        if j * diff > k:
            times = k // j
            remain = k % j
            tmp = times * (2 * pre - times + 1) // 2
            ans += tmp * j
            pre -= times
            ans += pre * remain
            break
        else:
            tmp = diff * (2 * pre - diff + 1) // 2
            ans += tmp * j
            k -= diff * j
        pre = p
        j += 1
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()