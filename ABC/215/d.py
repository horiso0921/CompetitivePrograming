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
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors
#solve
def solve():
    n,m = LI()
    a = LI()

    ans = [i for i in range(10 ** 5 + 1)]
    ans[0] = 0
    ans[1] = 0
    lis = []
    for ai in sorted(a):
        x = make_divisors(ai)
        for xi in x:
            lis.append(xi)
    lis = list(set(lis))
    
    for li in lis:
        if li != 1:
            if ans[li]:
                for l in range(li, 10 ** 5 + 1, li):
                    ans[l] = 0

    l = ["1"]
    for i in range(2, m+1):
        if ans[i]:
            l.append(str(i))
    print(len(l))
    print("\n".join(l))

    return


#main
if __name__ == '__main__':
    solve()