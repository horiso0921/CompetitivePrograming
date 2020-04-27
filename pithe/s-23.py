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

#A
def A():
    n, m, Q = LI()
    edg = [[0] * n for i in range(n)]
    check = defaultdict(int)
    for _ in range(m):
        a, b, f = LI_()
        edg[a][b] = f + 1
        edg[b][a] = f + 1
    q = []
    ded = defaultdict(int)
    for _ in range(Q):
        a, b = input().rsplit()
        b = int(b) - 1
        if a == "+":
            for i in range(n):
                if i == b:
                    continue
                if not check[i]:
                    heappush(q, -edg[b][i])
                else:
                    ded[edg[b][i]] += 1
            check[b] = 1
            h = -heappop(q)
            f = True
            while ded[h]:
                ded[h] -= 1
                if q:
                    h = -heappop(q)
                else:
                    print(0)
                    f = False
                    break
            if f:
                print(h)
                heappush(q, -h)
        else:
            for i in range(n):
                if i == b:
                    continue
                if check[i]:
                    if ded[edg[b][i]]:
                        ded[edg[b][i]] -= 1
                    else:
                        heappush(q, -edg[b][i])
                else:
                    ded[edg[b][i]] += 1
            check[b] = 0
            h = -heappop(q)
            f = True
            while ded[h]:
                ded[h] -= 1
                if q:
                    h = -heappop(q)
                else:
                    print(0)
                    f = False
                    break
            if f:
                print(h)
                heappush(q, -h)
    return

#Solve
if __name__ == '__main__':
    A()
