#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    a, b = LI()
    if (a * b) % 2:
        print("Yes")
    else:
        print("No")
    return

#B
def B():
    n = II()
    w = SR(n)
    d = []
    for i in w:
        d.append("".join(i))
    if len(set(d)) != n:
        print("No")
        return
    for i in range(n - 1):
        if w[i][-1] != w[i + 1][0]:
            print("No")
            return
    print("Yes")
    return

#C
def C():
    def gcd(a, b):
        a, b = max(a, b), min(a, b)
        while b:
            a, b = b, a % b
        return a
    n, x = LI()
    xn = LI()+[x]
    xn.sort()
    ans = xn[1] - xn[0]
    for i in range(1, n):
        ans = gcd(ans, xn[i + 1] - xn[i])
    print(ans)
    return

#D
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

#Solve
if __name__ == '__main__':
    D()

