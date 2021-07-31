
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
    II()
    a = LI()
    def f(suma, b):
        for i in a[1:]:
            if suma * (suma + i) < 0:
                suma += i
                continue
            b += (abs(suma + i) + 1)
            suma = (-1 * (suma > 0)) or 1
        return b

    if a[0] == 0:
        ans = min(f(1, 1), f(-1, 1))
    else:
        ans = min(f(a[0], 0), f(1 * (a[0] < 0) or - 1, abs(a[0]) + 1))
    print(ans)
    return

