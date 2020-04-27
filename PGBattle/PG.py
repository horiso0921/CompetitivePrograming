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

#A
def A():
    n = II()
    a = LI()
    a.sort()
    ans = inf
    for i in range(n):
        ans = min(ans, a[n + i] - a[i])
    print(ans)
    return

#B
def B():
    n = II()
    s = S()
    L = 1
    R = n
    if n & 1:
        for si in s:
            if si == "L":
                print(L)
                if L == R:
                    L = 2
                    R = n - 1
                else:
                    L += 2
            else:
                print(R)
                if L == R:
                    L = 2
                    R = n - 1
                else:
                    R -= 2
    else:
        c = [1] * n
        for si in s:
            if si == "L":
                if not c[L-1]:
                    if c[L-2]:
                        L -= 1
                        print(L)
                        c[L - 1] = 1
                        continue
                    if c[L]:
                        L += 1
                        print(L)
                        c[L - 1] = 1
                        continue
                if L - 1 == R:
                    if L == 1:
                        R = n - 1
                        print(L)
                    else:
                        if R == n:
                            L = 2
                            print(L)
                        else:
                            L = 2
                            R = n - 1
                            print(L)
                    c[L-1] = 0
                else:
                    print(L)
                    c[L-1] = 0
                    L += 2
            else:
                if not c[R-1]:
                    if c[R-2]:
                        R -= 1
                        print(R)
                        c[R - 1] = 1
                        continue
                    if c[R]:
                        R += 1
                        print(R)
                        c[R - 1] = 1
                        continue
                if L - 1 == R:
                    if L == 1:
                        R = n - 1
                        print(R)
                    else:
                        if R == n:
                            L = 2
                            print(R)
                        else:
                            L = 2
                            R = n - 1
                            print(R)
                    c[R-1] = 0
                else:
                    print(R)
                    c[R-1] = 0
                    R -= 2
    return

#C
def C():
    n = II()
    dp = [[0] * 3001 for i in range(3001)]
    xyd = LIR(n)
    for i in range(n):
        x, y, _ = xyd[i]
        dp[y][x] += 1
    for y in range(3001):
        for x in range(3001):
            dp[y][x] += dp[y][x - 1]
    for i in range(n):
        x, y, d = xyd[i]
        tmp = 0
        for yi in range(max(0, y - d), min(3000, y + d) + 1):
            tmp += dp[yi][min(3000, x + d - abs(y - yi))] - dp[yi][max(0, x - (d - abs(y - yi)) - 1)]
        print(tmp)
    return

#D
def D():
    n = II()
    a = LI()
    ans = 0
    for i in range(1, n - 1):
        if a[i - 1] < a[i] and a[i] > a[i + 1]:
            ans += min(a[i] - a[i - 1], a[i] - a[i + 1])
            a[i] = max(a[i - 1], a[i + 1])
        elif a[i - 1] > a[i] and a[i] < a[i + 1]:
            ans += min(a[i - 1] - a[i], a[i + 1] - a[i])
            a[i] = min(a[i - 1], a[i + 1])
    for i in range(n - 1):
        ans += abs(a[i] - a[i + 1])
    print(ans)

    return

#E
def E():
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
    C()
