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

def test(a):
    while len(a) != 1:
        tmp = []
        for i in range(len(a) - 2):
            tmp.append(sorted([a[i], a[i + 1], a[i + 2]])[1])
        a = tmp[::1]
    return tmp[0]
#solve
def solve():
    n, x = LI()
    if 1 == x or 2 * n - 1 == x:
        print("No")
        return
    print("Yes")
    if x < n:
        for i in range(n, 0, -1):
            if i == x:
                continue
            print(i)
        print(x)
        for i in range(n + 1, 2 * n):
            print(i)
    elif x == n:
        for i in range(1, 2 * n):
            print(i)
    else:
        for i in range(1, n):
            print(i)
        print(x)
        for i in range(2 * n - 1, n - 1, -1):
            if i == x:
                continue
            print(i)



#main
if __name__ == '__main__':
    solve()
