
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
def A():
    _ = II()
    a = LI()
    a.sort()
    x = list(set(a))
    if len(x) > 3:
        print("No")
    elif len(x) == 3:
        x.sort()
        x1 = bisect_right(a, x[0])
        x2 = bisect_right(a, x[1]) - bisect_left(a, x[1])
        x3 = bisect_right(a, x[2]) - bisect_left(a, x[2])
        if ((x[0] ^ x[1] ^ x[2]) == 0) and (x1 == x2 == x3):
            print("Yes")
        else:
            print("No")
    elif len(x) == 2:
        x1 = bisect_right(a, 0)
        x2 = bisect_right(a, x[1]) - bisect_left(a, x[1])
        if x1 * 2 == x2:
            print("Yes")
        else:
            print("No")
    elif len(x) == 1:
        if x[0] == 0:
            print("Yes")
        else:
            print("No")
    return
