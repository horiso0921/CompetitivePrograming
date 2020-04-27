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
inf = 1e10

#solve
def solve():
    h, w = LI()
    s = SR(h)
    def bfs(x, y):
        xy_ = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        count1 = 1
        count2 = 0
        q = deque([])
        q.append((x,y))
        while q:
            x,y = q.popleft()
            for xy in xy_:
                x_, y_ = x + xy[0], y + xy[1]
                if 0 <= x_ < w and 0 <= y_ < h:
                    if s[y_][x_] != s[y][x] and field[y_][x_]:
                        field[y_][x_] = False
                        if s[y_][x_] == "#":
                            count1 += 1
                        else:
                            count2 += 1
                        q.append((x_, y_))
        return count1*count2
                        
    field = [[True for i in range(w)] for k in range(h)]
    ans = 0
    for y in range(h):
        for x in range(w):
            if s[y][x] == "#" and field[y][x]:
                field[y][x] = False
                ans += bfs(x, y)
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
