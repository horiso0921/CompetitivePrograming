#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import *
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

#A
def A():
    l, x = LI()
    i = 1
    while x > 0:
        x -= l
        i ^= 1
    if i == 0 and x == 0:
        print(l)
        return
    print((-1 * i or 1) * x % l)
    return

#B
def B():
    n,d = LI()
    s = SR(d)
    ans = 0
    for i in range(d):
        for k in range(i+1, d):
            tmp = [0] * n
            for j in range(n):
                if s[i][j] == "o":
                    tmp[j] = 1
                if s[k][j] == "o":
                    tmp[j] = 1
            ans = max(ans, sum(tmp))
    print(ans)
    return

#C
def C():
    n, d = LI()
    r = LI()
    r.sort()
    ans = 0
    for num, i in enumerate(r, start=1):
        b = bisect_right(r, i + d)
        ans += max(0, (b - num) * (b - num - 1) // 2)
    print(ans)
    return

#D
def D():
    n, K = LI()
    a = LI()
    d = defaultdict(int)
    i = 0
    while i < n-1:
        for k in range(i + 1, n):
            if a[i] == a[k]:
                continue
            d[k - i] += 1
            i = k
            break
        else:
            d[k - i+1] += 1
            i = k
    for i in range(1, n + 1):
        b = 0
        for key, value in d.items():
            b += (key // (i + 1)) * value
            if b <= K:
                continue
            break
        else:
            print(i)
            return
    return

#E
def E():
    n = II()
    s = S()
    a, b, c, d = LI()
    
    return

#F
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
