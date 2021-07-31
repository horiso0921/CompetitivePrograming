
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
r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
field = ["#"*(c+2)]+["#"+input()+"#" for i in range(r)]+["#"*(c+2)]
check =[[0 for i in range(c+2)] for i in range(r+2)]
import queue
player = queue.Queue()

player.put((sy, sx, 0))
while not player.empty():
    now = player.get()
    x = [0, 1, 0, -1]
    y = [-1, 0, 1, 0]
    for i in range(4):
        if field[now[0] + y[i]][now[1] + x[i]] == "." and check[now[0] + y[i]][now[1] + x[i]] == 0:
            player.put((now[0] + y[i], now[1] + x[i], now[2] + 1))
            check[now[0] + y[i]][now[1] + x[i]] = 1
            if now[0] + y[i] == gy and now[1] + x[i] == gx:
                print(now[2] + 1)
                quit()


