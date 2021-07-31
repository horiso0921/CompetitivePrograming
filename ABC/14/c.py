
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
    n = I()
    ab = LIR(n)
    ans = 0
    heho = [0 for i in range(10 ** 3 + 1)]
    moto = [0 for i in range(10 ** 6 + 1)]
    for a,b in ab:
        hehoa = 1 + a // 10 ** 3
        hehob = b // 10 ** 3
        for i in range(a, min(hehoa * 10 ** 3, b+1)):
            moto[i] += 1
        for i in range(max(hehob,hehoa) * 10 ** 3, b + 1):
            moto[i] += 1
        for i in range(hehoa, hehob):
            heho[i] += 1
    for num, i in enumerate(moto):
        ans = max(ans, i + heho[num // 10 ** 3])
    print(ans)

