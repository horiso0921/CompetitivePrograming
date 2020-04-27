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
    x = S()
    ans = 0
    for i in x:
        ans += int(i)
    print(ans)
    return

#B
def B():
    n = II()
    s = S()
    s = "".join(s)
    d = defaultdict(lambda: -1)
    x = deque()
    x.append("b")
    d["".join(x)] = 0
    for i in range(1,n):
        if i % 3 == 1:
            x.append("c")
            x.appendleft("a")
        elif i % 3 == 2:
            x.append("a")
            x.appendleft("c")
        else:
            x.append("b")
            x.appendleft("b")
        d["".join(x)] = i
    print(d["".join(s)])
    return

#C
def C():
    R, C, K = LI()
    n = II()
    rc = LIR_(n)
    fldr = [0 for _ in range(R)]
    fldc = [0 for _ in range(C)]
    for r, c in rc:
        fldr[r] += 1
        fldc[c] += 1
    fldcs = fldc[::1]
    fldcs.sort()
    fldrs = fldr[::1]
    fldrs.sort()
    ans = 0
    for k in range(K+1):
        ans += (bisect.bisect_right(fldcs, K - k) - bisect.bisect_left(fldcs, K - k)) * (bisect.bisect_right(fldrs, k) - bisect.bisect_left(fldrs, k))
    for r, c in rc:
        a = fldr[r] + fldc[c]
        if a == K:
            ans -= 1
        elif a == K + 1:
            ans += 1
    print(ans)
    return

#D
def D():
    def f(x):
        T = [0] * n
        for h, s in hs:
            t = (x - h) // s
            if t < n:
                T[t] += 1
        y = 0
        for num, t in enumerate(T):
            y += t
            if num + 1 < y:
                return False
        return True
    n = II()
    hs = LIR(n)
    l = 0
    r = 0
    for h, s in hs:
        l = max(l, h - 1)
        r = max(r, h + (n - 1) * s)
    while r - l > 1:
        m = (l + r) // 2
        if f(m):
            r = m
        else:
            l = m
    print(r)
    
    return

#Solve
if __name__ == '__main__':
    D()
