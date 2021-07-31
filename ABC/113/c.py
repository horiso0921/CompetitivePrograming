
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
    n, m = LI()
    py = LIR(m)
    pya = py[::1]
    py.sort(key=lambda x: x[1])
    city = [1 for i in range(n)]
    dicity = {}
    for p, y in py:
        dicity[(p,y)] = city[p-1]
        city[p-1] += 1    
    for p, y in pya:
        a = "00000" + str(p)
        a = a[-6:]
        b = "00000" + str(dicity[(p, y)])
        b = b[-6:]
        print(a+b)

    return

