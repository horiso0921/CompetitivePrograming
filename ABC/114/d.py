
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
def D():
    n = II()
    primelis = primes(100)
    d = {2: 0, 4: 0, 14: 0, 24: 0, 74: 0}
    for i in primelis:
        b = n
        tmp = 0
        while b // i:
            tmp += (b // i)
            b = (b // i)
        for x in d.keys():
            d[x] += (tmp >= x)
    ans = 0
    ans += (d[2] - 1) * d[24]
    ans += (d[4] - 1) * d[14]
    ans += d[74]
    ans += (d[2] - 2) * (d[4] - 1) * d[4] // 2
    print(ans)
    return

