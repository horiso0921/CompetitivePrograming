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
inf = float('INF')

#solve
def solve():
    n = II()
    a = LI()
    ma = [None] * (n + 1)
    tmp = 0
    for i in range(n, -1, -1):
        x = pow(2, i)
        tmp += a[i]
        if tmp <= x:
            tmp = (tmp - 1) // 2 + 1
            continue
        else:
            print(-1)
            return
    ma[n] = a[-1]
    for i in range(n - 1, -1, -1):
        ma[i] = min(pow(2, i), ma[i + 1] + a[i])
    tmp = 1
    ans = 1
    for i in range(1, n + 1):
        tmp = tmp * 2
        ans += min(tmp, ma[i])
        tmp = min(tmp, ma[i])
        tmp -= a[i]
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
