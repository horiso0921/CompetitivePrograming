
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
    move = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    h, w = LI()
    s = SR(h)
    q = deque([(0, 0, 1)])
    ans = h * w
    for y in range(h):
        for x in range(w):
            if s[y][x] == "#":
                ans -= 1
    check = [[True] * w for _ in range(h)]
    while q:
        x, y, tern = q.pop()
        for mx, my in move:
            mx += x
            my += y
            if 0 <= mx < w and 0 <= my < h:
                if s[my][mx] == "." and check[my][mx]:
                    check[my][mx] = False
                    if my == h - 1 and mx == w - 1:
                        print(ans - tern - 1)
                        return
                    q.appendleft((mx, my, tern + 1))
    print(-1)


    return
