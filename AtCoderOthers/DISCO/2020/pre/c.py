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
    h, w, k = LI()
    s = SR(h)
    done = []
    ans = [[None] * w for i in range(h)]
    for y in range(h):
        f = 0
        for x in range(w):
            if f:
                if s[y][x] == "#":
                    k -= 1
                ans[y][x] = str(k)
            else:
                if s[y][x] == "#":
                    f = 1
                ans[y][x] = str(k)
        if f:
            done.append(y)
            k -= 1
    
    for d in done:
        for y in range(d + 1, h):
            if y in done:
                break
            ans[y] = ans[d]
        for y in range(d - 1, -1, -1):
            if y in done:
                break
            ans[y] = ans[d]
    
    for a in ans:
        print(" ".join(a))

    return


#main
if __name__ == '__main__':
    solve()
