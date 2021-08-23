
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
def B():
    n = II()
    s = SR(n)
    edg = [[] for i in range(n)]
    check = [0] * n
    for i in range(n):
        for k in range(n):
            if i == k:
                continue
            if s[i][k]:
                edg[i].append(k)
                edg[k].append(i)
            else:
                s[i][k] = inf
    for i in range(n):
        q = deque([i])
        if check[i] == 0:
            check[i] += 1
        while q:
            p = q.pop()
            for k in edg[p]:
                if check[k]:
                    if (check[k] ^ check[p]) & 1:
                        continue
                    print(-1)
                    return
                else:
                    check[k] = check[p] + 1
                    q.appendleft(k)
    for x in range(n):
        for i in range(n):
            for k in range(n):
                s[i][k] = min(s[i][k], s[i][x] + s[x][k])
    ans = 0
    for i in range(n):
        for k in range(n):
            if s[i][k] == inf:
                continue
            ans = max(s[i][k], ans)
    print(ans+1)
