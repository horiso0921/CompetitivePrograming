#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
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
    m = II()
    s1, s2 = LS()
    s1 = sorted(list(set(s1)))
    s2 = sorted(list(set(s2)))
    t = LSR(m)
    ans = []
    for ai in range(26):
        a = chr(ord("a") + ai)
        for bi in range(26):
            b = chr(ord("a") + bi)
            if a in s1 and b in s2:
                ans.append(a+b)
    for a12 in ans:
        for t1, t2 in t:
            a1 = a12[0]
            a2 = a12[1]
            if not (a1 in t1 and a2 in t2):
                print("Yes")
                print(a12)
                return
    print("No")
    return


#main
if __name__ == '__main__':
    solve()