
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
    h, w = LI()
    d = []
    for y in range(h):
        a = LI()
        tmp = []
        for x in range(w):
            if a[x] & 1:
                tmp.append((y,x))
        for t in tmp[::-1 if y & 1 else 1]:
            d.append(t)
    ans = []
    for i in range(0, len(d) - 1, 2):
        y, x = d[i]
        next_y, next_x = d[i + 1]
        for ny in range(y, next_y + 1):
            for nx in range(x, -1 if ny & 1 else w, -1 if ny & 1 else 1):
                if y == ny and x == nx:
                    continue
                ans.append((y+1, x+1, ny+1, nx+1))
                if ny == next_y and nx == next_x:
                    break
                y = ny
                x = nx
    print(len(ans))
    for a in ans:
        print(*a)
    return

