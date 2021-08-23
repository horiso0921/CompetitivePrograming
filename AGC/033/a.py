
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
def A():
    h, w = LI()
    A = SR(h)
    check = [[True for _ in range(w)] for i in range(h)]
    q = deque([])
    for tate in range(h):
        for yoko in range(w):
            if A[tate][yoko] == "#":
                q.append((tate, yoko))
                check[tate][yoko] = False
    new_q = deque([])
    ans = 0
    while True:
        while q:
            y, x = q.pop()
            for movex, movey in xy:
                if 0 <= y + movey < h and 0 <= x + movex < w and check[y + movey][x + movex]:
                    check[y + movey][x + movex] = False
                    new_q.append((y + movey, x + movex))
        if not new_q:
            break
        ans += 1
        q = new_q
        new_q = deque([])
    print(ans)
                    

        
    return

