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
    n = II()
    s = S()
    ans = list(s)
    def f(l, r, c):
        if ord(c) == ord("z") + 1: return
        L = l
        last = r
        for i in range(r, l-1, -1):
            if L >= i:
                f(L, last, chr(ord(c) + 1))
                break
            if s[i] == c:
                while L < i and s[L] <= c:
                    L += 1
                if L < i:
                    ans[L] = s[i]
                    ans[i] = s[L]
                    last = i
                    L += 1
    f(0, n-1, "a")
    print("".join(ans))
            
    return


#main
if __name__ == '__main__':
    solve()