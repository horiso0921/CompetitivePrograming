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
def S(): return input().rstrip()
def LS(): return S().split()
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
    def root(x):
        if x == par[x]:
            return x
        par[x] = root(par[x])
        return par[x]

    def unite(x, y):
        x = root(x)
        y = root(y)
        if y < x:
            x, y = y, x
        par[y] = x
        return True

    def f(x):
        if "0" <= x <= "9":
            return int(x)
        else:
            return ord(x) - ord("A") + 10

    par = [i for i in range(36)]
    n = II()
    s1 = S()
    s2 = S()
    c = [0] * 36
    for si in s1 + s2:
        if "0" <= si <= "9":
            c[int(si)] = 1
        else:
            c[ord(si) - ord("A") + 10] = 1
    for i in range(n):
        unite(f(s1[i]), f(s2[i]))
    
    for i in range(36):
        root(i)
    ch = [0] * 36
    for i in range(10, 36):
        if c[i]:
            if 0 <= root(i) < 10:
                continue
            ch[root(i)] = 1

    if sum(ch):
        ans = 9
        if 0 <= root(f(s1[0])) <= 9 or 0 <= root(f(s2[0])) <= 9:
            ans = 10
        print(ans * (10 ** (sum(ch) - 1)))
    else:
        print(1)


    return


#main
if __name__ == '__main__':
    solve()
