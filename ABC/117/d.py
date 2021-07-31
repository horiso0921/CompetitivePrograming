
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
    x = LI()
    ans = 0
    mae = 0
    b = [0] * 40
    for i in range(40):
        for k in x:
            b[i] += (k & (1 << i)) >> i
    c = [0] * 40
    for i in range(39):
        if b[i] > n - b[i]:
            c[i+1] = c[i] + (b[i] << i)
        else:
            c[i+1] = c[i] + (n - b[i] << i)
    for i in range(39, -1, -1):
        if m & (1 << i):
            ansb = mae
            ansb += b[i] << i
            ansb += c[i]
            if ans < ansb:
                ans = ansb
            mae += n - b[i] << i
        else:
            mae += b[i] << i
    ans = max(ans, mae)
    print(ans)
    return

