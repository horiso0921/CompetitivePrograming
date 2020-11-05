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
inf = float("INF")

#solve
def solve():
    n = II()
    xy = LIR(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and i != k and j != k:
                    xi,yi = xy[i]
                    xj,yj = xy[j]
                    xk,yk = xy[k]
                    vec1 = (xj - xi, yj - yi)
                    vec2 = (xk - xi, yk - yi)
                    naiseki = (vec1[0] * vec2[0] + vec1[1] * vec2[1]) ** 2
                    ookisa1 = vec1[0] ** 2 + vec1[1] ** 2
                    ookisa2 = vec2[0] ** 2 + vec2[1] ** 2
                    if naiseki == ookisa1 * ookisa2 or naiseki == - ookisa1 * ookisa2:
                        print("Yes")
                        return
    print("No")
    return
                
        
    return


#main
if __name__ == '__main__':
    solve()
