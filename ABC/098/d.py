
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
    a = LI()
    bitlength = len(bin(max(a))) - 2
    a = list(map(lambda x: bin(x)[:1:-1], a))
    cumulativebit = [[0] * bitlength for i in range(n)]
    for i in range(n):
        for bi in range(bitlength):
            cumulativebit[i][bi] += cumulativebit[i - 1][bi] + (0 if len(a[i]) <= bi else 1 if int(a[i][bi]) else 0)
    r = 0
    ans = 0
    for l in range(n):
        f = False
        cumulativebitl = cumulativebit[l]
        al = a[l]
        for r in range(r, n):
            cumulativebitr = cumulativebit[r]
            ar = a[r]
            for bi in range(bitlength):
                if cumulativebitr[bi] - cumulativebitl[bi] >= 2 or (l != r and len(ar) > bi and len(al) > bi and int(ar[bi]) and int(al[bi])):
                    f = True
                    break
            if f:
                break
        if f:
            ans += r - l
        else:
            ans += r - l + 1
    print(ans)
    return



