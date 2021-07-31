
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
    ab = LIR_(n - 1)
    edg = [[] for i in range(n)]
    for a,b in ab:
        edg[a].append(b)
        edg[b].append(a)
    check = defaultdict(int)
    chb = defaultdict(lambda: True)
    ans = k
    q = deque()
    for i in edg[0]:
        check[i] = 1
        q.append(i)
    check[0] = 1
    chb[0] = False
    while q:
        i = q.pop()
        chb[i] = False
        b = 0
        x = 0
        for e in edg[i]:
            b += check[e]
            check[e] += 1
            if chb[e]:
                q.appendleft(e)
            else:
                x += 1
        check[i] = x + 1
        ans *= (k - b)
        ans %= mod
    print(ans)
    return

