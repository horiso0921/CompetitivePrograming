
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
    n, c = LI()
    D = LIR(c)
    C = LIR_(n)
    CL = list(itertools.permutations(range(c), 3))
    ans = inf
    amari0 = [0 for i in range(30)]
    amari1 = amari0[::1]
    amari2 = amari0[::1]
    for y in range(n):
        for x in range(n):
            amari = (x + y) % 3
            if amari == 0:
                amari0[C[y][x]] += 1
            if amari == 1:
                amari1[C[y][x]] += 1
            if amari == 2:
                amari2[C[y][x]] += 1
    for c0, c1, c2 in CL:
        ansb = 0
        for i in range(c):
            ansb += D[i][c0] * amari0[i]
            ansb += D[i][c1] * amari1[i]
            ansb += D[i][c2] * amari2[i]
        ans = min(ans, ansb)
    print(ans)
    return

