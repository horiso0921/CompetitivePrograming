
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
    N = II()
    a = LI()
    b = LI()
    ans = 0
    t = 1
    for i in range(29):
        a2 = [A & ((t << 1) - 1) for A in a]
        b2 = [B & ((t << 1) - 1) for B in b]
        a2.sort(reverse=True)
        b2.sort()
        ansb = r1 = r2 = r3 = 0
        for A in a2:
            while r1 < N and A + b2[r1] < t:
                r1 += 1
            while r2 < N and A + b2[r2] < 2*t:
                r2 += 1
            while r3 < N and A + b2[r3] < 3*t:
                r3 += 1
            ansb += r2 ^ r1 ^ N ^ r3
            ansb = ansb & 1
        ans += (ansb << i)
        t = t << 1
    print(ans)
    return

