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
    k = II()
    x, y = II()
    fx = 1 if x < 0 else 0
    fy = 1 if y < 0 else 0
    x, y = abs(x), abs(y)
    ty = abs(y - x % k)
    
    ans = [[0,0]]
    while ans[-1][0] != x:
        tmp = [ans[-1][0], ans[-1][1]]
        tmp[0] += k
        if tmp[0] > k:
            tmp[1] += tmp[0] - k
            tmp[0] = k
        ans.append(tmp)
    while ans[-1][1] != y:
        tmp = [ans[-1][0], ans[-1][1]]
        
    return


#main
if __name__ == '__main__':
    solve()
