
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
def C():
    h, w, t = LI()
    s = SR(h)
    xy = [(0, -1), (1, 0), (-1, 0), (0, 1)]
    for y in range(h):
        for x in range(w):
            if s[y][x] == "S":
                start = (y, x)
            if s[y][x] == "G":
                goal = (y, x)
                
    def bfs(n):
        check = [[inf for _ in range(w)] for __ in range(h)]
        q = deque()
        q.append(start)
        check[start[0]][start[1]] = 0
        while q:
            y, x = q.pop()
            for y_, x_ in xy:
                if 0 <= y + y_ < h and 0 <= x + x_ < w:
                    if s[y + y_][x + x_] == "#":
                        if check[y][x] + n < check[y+y_][x+x_]:
                            check[y+y_][x+x_] = check[y][x] + n
                            q.append((y + y_, x + x_))
                    else:
                        if check[y][x] + 1 < check[y+y_][x+x_]:
                            check[y+y_][x+x_] = check[y][x] + 1
                            q.append((y + y_, x + x_))
        if check[goal[0]][goal[1]] <= t:
            return True
        else:
            return False
    lo = 1
    hi = t+1
    while 1:
        mi = (lo + hi) // 2
        if bfs(mi):
            lo = mi
        else:
            hi = mi
        if hi - lo == 1:
            break
    print(lo) 
    return

