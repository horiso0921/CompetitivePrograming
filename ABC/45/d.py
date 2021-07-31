
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
    h, w, n = LI()
    ans = [(h - 2) * (w - 2)] + [0] * 9
    d = defaultdict(int)
    for _ in range(n):
        a, b = LI()
        for mb in range(-1, 2):
            mb += b
            for ma in range(-1, 2):
                if mb == ma == 0:
                    continue
                ma += a
                if 2 <= ma < h and 2 <= mb < w:
                    d[(ma, mb)] += 1
    for _, value in d.items():
        ans[value] += 1
        ans[0] -= 1
    print("\n".join(map(str, ans)))
    return

