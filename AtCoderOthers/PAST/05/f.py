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
def LFR(n): return [LF() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    n,m = LI()
    abc = LIR_(m)
    ans = 0
    for mask in range(1 << n):
        f = 1
        tx = [0] * n
        for a_b_c in abc:
            tmp = []
            for a in a_b_c:
                if mask & (1 << a):
                    tmp.append(a)
            if len(tmp) == 3:
                f = 0
            elif len(tmp) == 2:
                a = set(a_b_c) ^ set(tmp)
                for ai in a:
                    tx[ai] = 1 
        if f:
            ans = max(ans, sum(tx))
    print(ans)         
    return


#main
if __name__ == '__main__':
    solve()