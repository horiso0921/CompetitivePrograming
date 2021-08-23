
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
    edg = [[] for i in range(n)]
    for _ in range(n - 1):
        a, b = LI_()
        edg[a].append(b)
        edg[b].append(a)
    rank = [0] * n
    q = deque()
    q.append(0)
    rank[0] = 1
    while q:
        p = q.pop()
        for i in edg[p]:
            if rank[i]:
                continue
            rank[i] = rank[p] + 1
            q.appendleft(i)
    k = 2
    q = deque()
    q.append(n - 1)
    while q:
        p = q.pop()
        for i in edg[p]:
            if rank[i] < rank[p]:
                if rank[i] <= k:
                    a = p
                    break
                q.appendleft(i)
                k += 1
    ans1 = 1
    ans2 = 1
    check = [True] * n
    q = deque()
    q.append(a)
    check[a] = False
    while q:
        p = q.pop()
        for i in edg[p]:
            if rank[i] > rank[p]:
                q.append(i)
                ans1 += 1
                check[i] = False
    q = deque()
    q.append(0)
    check[0] = False
    while q:
        p = q.pop()
        for i in edg[p]:
            if check[i]:
                q.append(i)
                ans2 += 1
                check[i] = False
    print(["Fennec", "Snuke"][ans1 >= ans2])
    return

