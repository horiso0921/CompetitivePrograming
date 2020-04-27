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
    c_f, c_b = LI()
    a = 0
    for i, si in enumerate(S(), start=1):
        if si == "s":
            a += 1 << (n - i)
    dp = [[[inf] * (1 << n) for i in range(1 << n)] for i in range(n)]
    q = []
    q.append([0, 0, a, [0]])
    while q:
        score, done, safe, route = heappop(q)
        now = route[-1]
        if done == (1 << n) - 1 and now == 0:
            break
        for i in range(n):
            if i == now:
                continue
            if safe >> i & 1:
                b_safe = safe
                for k in range(i):
                    b_safe ^= 1 << k
                if now < i:
                    if score + c_b < dp[i][done | 1 << i][b_safe]:
                        dp[i][done | 1 << i][b_safe] = score + c_b
                        heappush(q, [score + c_b, done | 1 << i, b_safe, route+[i]])
                else:
                    if score + c_f < dp[i][done | 1 << i][b_safe]:
                        dp[i][done | 1 << i][b_safe] = score + c_f
                        heappush(q, [score + c_f, done | 1 << i, b_safe, route+[i]])
    print(" ".join(map(str, map(lambda x: abs(n-x), route))))
    return

#Solve
if __name__ == '__main__':
    A()
