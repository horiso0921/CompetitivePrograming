#!usr/bin/env python3
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

# A
def A():
    while True:
        n = II()
        if not n:
            break
        a = IR(n)
        a.sort()
        print(sum(a[1:-1])//(n-2))
            
    return

# B
def B():
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while True:
        w, h = LI()
        if w == h == 0:
            break
        field = SR(2 * h - 1)
        check = [[True] * (2 * w - 1) for i in range(2 * h - 1)]
        next = deque()
        next.append((0, 0))
        ans = 1
        flg = True
        
        while next and flg:
            now = next
            next = deque()
            while now:
                x, y = now.pop()
                for mx, my in move:
                    mmx, mmy = x + mx, y + my
                    if 0 <= mmx < 2 * w - 1 and 0 <= mmy < 2 * h - 1:
                        if field[mmy][mmx] == '0' and check[mmy+my][mmx+mx]:
                            next.append((mmx + mx, mmy + my))
                            check[mmy + my][mmx + mx] = False
                            if mmx+mx == 2 * w - 2 and mmy+my == 2 * h - 2:
                                print(ans+1)
                                flg = False
                                next = deque()
                                now = deque()
                                break
            ans += 1
        if flg:
            print(0)
    return

# C
def C():
    while 1:
        r, n = LI()
        if r == n == 0:
            break
        lis = [0 for i in range(2 * r)]
        ans = inf
        for _ in range(n):
            xl, xr, h = LI()
            for i in range(2 * r):
                if xl+r <= i < xr+r:
                    lis[i] = max(lis[i], h)
        for i in range(2 * r):
            if i < r:
                ans = min(ans, r - math.sqrt((r ** 2 - (r - i - 1)** 2)) + lis[i])
            else:
                ans = min(ans, r - math.sqrt((r ** 2 - (r - i)** 2)) + lis[i])
        print(ans)
    return

# D
def D():
    fact = [1 for i in range(1000001)]
    fact[1] = 0
    z = 2
    while 1:
        j = 2
        while z*j < 1000001:
            fact[z*j] = 0
            j += 1
        for j in range(z+1,1000001):
            if fact[j]:
                z = j
                break
        else:
            break
    def DFS(n):
        if n == 0:
            return 1
        return DFS(n - 1)
    print(DFS(10**4))
    return

# E
def E():
    return

# F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    D()
