#!/usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys
import random
import itertools
import math
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
inf = 1e10
#solve


def solve():
    n, m = LI()
    a = LI()
    a0 = a[0]
    bi = 0
    while not (a0 & 1):
        bi += 1
        a0 >>= 1
    if not bi:
        print(0)
        return
    for ai in a[1:]:
        tmp = 0
        while not (ai & 1):
            tmp += 1
            ai = ai >> 1
        if tmp == bi:
            continue
        print(0)
        return

    def lcm(a):
        from fractions import gcd
        x = a[0]
        for i in range(1, len(a)):
            x = (x * a[i]) // gcd(x, a[i])
        return x
    lc = lcm(list(map(lambda x: x >> 1, set(a))))
    print((m + lc) // lc // 2)
    return


#main
if __name__ == '__main__':
    solve()
