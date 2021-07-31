
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
    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    h, w = LI()
    II()
    a = LI()
    ans = [[None] * w for i in range(h)]
    x = 0
    y = 0
    diarect = 0
    for num, ai in enumerate(a, start=1):
        for _ in range(ai):
            ans[y][x] = num
            x += move[diarect][0]
            y += move[diarect][1]
            if 0 <= x < w and 0 <= y < h:
                if ans[y][x]:
                    x -= move[diarect][0]
                    y -= move[diarect][1]
                    diarect += 1
                    diarect %= 4
                    x += move[diarect][0]
                    y += move[diarect][1]
                continue
            x -= move[diarect][0]
            y -= move[diarect][1]
            diarect += 1
            diarect %= 4
            x += move[diarect][0]
            y += move[diarect][1]
            
    for a in ans:
        print(" ".join(map(str, a)))
    return

