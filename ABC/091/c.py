
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
    n = II()
    ab = LIR(n)
    cd = LIR(n)
    ab.sort()
    cd.sort()
    check = [0 for i in range(n)]
    ans = 0
    for _, c in enumerate(cd):
        d = c[1]
        c = c[0]
        maxy = -1
        x = -1
        for k, a in enumerate(ab):
            b = a[1]
            a = a[0]
            if maxy < b and c > a and check[k] == 0 and d > b:
                maxy = b
                x = k
        if x != -1:
            ans += 1
            check[x] += 1
    print(ans)


    return

