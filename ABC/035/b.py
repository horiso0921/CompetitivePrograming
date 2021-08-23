
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
    s = S()
    t = II()
    now = [0, 0]
    q = 0
    d = defaultdict(int)
    d["U"] = (0, 1)
    d["L"] = (-1, 0)
    d["R"] = (1, 0)
    d["D"] = (0, -1)
    for i in s:
        if i == "?":
            q += 1
            continue
        now = [now[0] + d[i][0], now[1] + d[i][1]]
    x,y = map(abs,now)
    if t == 1:
        print(y + x + q)
        return
    if x + y >= q:
        print(x + y - q)
        return
    q -= x + y
    print(q % 2)
    return

