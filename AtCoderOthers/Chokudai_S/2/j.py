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
    n = II()
    ab = LIR(n)
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    ans = [ab[0][0],  ab[0][1]]
    for a, b in ab[1:]:
        an1 = []
        for key in ans:
            an1.append(gcd(key, a))
            an1.append(gcd(key, b))
        an1 = list(set(an1))
        ans = []
        for a in an1:
            for b in an1:
                if a != b:
                    if b % a == 0:
                        break
            else:
                ans.append(a)
    print(max(ans))
    return


#main
if __name__ == '__main__':
    solve()
