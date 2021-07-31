
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
def E():
    n, k = LI()
    if k > (n - 1) * (n - 2) / 2:
        print(-1)
        return
    d = (n - 1) * (n - 2) // 2 - k
    a = [[] for i in range(n)]
    for i in range(n):
        if i != 1:
            a[i].append(1)
            a[1].append(i)
    l = 0
    m = 2
    while d > 0:
        a[l].append(m)
        m += 1
        d -= 1
        if m == n:
            l += 1
            m = l + 1
            if l == 1:
                l = 2
                m = 3
    aa = 0
    ans = []
    for num,i in enumerate(a):
        for l in i:
            if num < l:
                aa += 1
                ans.append((num+1,l+1))
    print(aa)
    for x, y in ans:
        print(x, y)
    return

