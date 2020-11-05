#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for _ in range(n)]
def LIR(n):
    return [LI() for _ in range(n)]
def SR(n):
    return [S() for _ in range(n)]
def LSR(n):
    return [LS() for _ in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007
D = {(1,0),(-1,0),(0,1),(0,-1)}
def solve():
    def bfs(y,x,d):
        q = [(y,x)]
        start = s[y][x]
        check = [[0]*n for _ in range(n)]
        s[y][x] = d
        check[y][x] = 1
        cn = {i:0 for i in range(1,k+1)}
        for y,x in q:
            for dy,dx in D:
                ny,nx = y+dy,x+dx
                if 0 <= ny < n and 0 <= nx < n:
                    if s[ny][nx] == start:
                        if not check[ny][nx]:
                            check[ny][nx] = 1
                            s[ny][nx] = d
                            q.append((ny, nx))
                    else:
                        if not check[ny][nx] and s[ny][nx] != d:
                            check[ny][nx] = 1
                            cn[s[ny][nx]] += 1
        return cn

    _,n,k = LI()
    s = [list(map(int, input())) for _ in range(n)]
    cnt = {g: 0 for g in range(1, k + 1)}
    x = n // 2
    y = n // 2
    cnt[s[y][x]] = -1
    for dy,dx in D:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n and s[ny][nx] != s[y][x]:
            cnt[s[ny][nx]] += 1
    ans = []
    cnt = list(cnt.items())
    cnt.sort(key=lambda x: -x[1])
    d = cnt[0][0]
    while 1:
        cnt = bfs(x, y, d)
        cnt = list(cnt.items())
        cnt.sort(key=lambda x: -x[1])
        ans.append((x + 1, y + 1, d))
        if cnt[0][1] == 0:
            break
        d = cnt[0][0]
    print(len(ans))
    for y,x,d in ans:
        print(y,x,d)
    return

#Solve
if __name__ == "__main__":
    solve()
