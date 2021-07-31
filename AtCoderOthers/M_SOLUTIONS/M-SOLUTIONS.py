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
mod = 10**6+3
inf = float('INF')

# A
def A():
    n = II()
    print((n-2)*180)
    return

# B
def B():
    b = S()
    kati = b.count("o")
    kati += 15 - len(b)
    if kati >= 8:
        print("YES")
    else:
        print("NO")
    return

# C
def C():
    n, a, b, c = LI()
    def Moth(q, n):
        if n == 0:
            return 1
        if n % 2:
            return q * Moth(q*q, n //2) % mod
        else:
            return Moth(q * q, n // 2)
    print(Moth(4,mod-2))

    return

# D
def D():
    n = II()
    ab = LIR_(n-1)
    C = LI()
    C.sort(reverse=True)
    c = deque()
    for ci in C:
        c.appendleft(ci)
    edg = [[] for i in range(n)]
    for a, b in ab:
        edg[a].append(b)
        edg[b].append(a)
    for num,e in enumerate(edg):
        if len(e) == 1:
            start = num
            break
    q = deque()
    ans = [0 for i in range(n)]
    q.append(start)
    ans[start] = c.pop()
#    print(start)
    while q:
        p = q.pop()
        for e in edg[p]:
            if not ans[e]:
                ans[e] = c.pop()
                q.append(e)
    anssum = 0
    for a, b in ab:
        anssum += min(ans[a], ans[b])
    print(anssum)
    ans = list(map(str, ans))
    print(" ".join(ans))


    return

# E
def E():
    q = II()
    for _ in range(q):
        x, d, n = LI()
        ans = math.pow(x, n) % mod
        ans *= math.gamma(x / d + n) % mod
        ans /= math.gamma(x / d)
        ans %= mod
        print(ans)
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
    C()
