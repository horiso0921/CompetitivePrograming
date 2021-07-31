
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
    n, m = LI()
    a = LI()
    bc = LIR(m)
    bc.sort(key=lambda x: x[1], reverse=True)
    a.sort()
    index = 0
    suma = 0
    for b, c in bc:
        if index + b >= n:
            if a[n - 1] <= c:
                suma += (n - index) * c
            else: 
                br = bisect_left(a, c)
                if br > index:
                    suma += (br - index) * c
                    index = br
                    break
                else:
                    break
            index = n
            break
        if a[index + b - 1] < c:
            suma += b * c
            index += b
        else:
            if a[index] < c:
                bl = bisect_left(a, c)
                suma += (bl - index) * c
                index = bl
            else:
                break
    suma += sum(a[index:])
    print(suma)

    return

