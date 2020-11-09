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
def IR(n):
    res = [None] * n
    for i in range(n):
        res[i] = II()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI()
    return res
def FR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIF(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def SR(n):
    res = [None] * n
    for i in range(n):
        res[i] = S()
    return res
def LSR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LS()
    return res
mod = 1000000007
inf = float('INF')

#solve
def solve(n):
    w = SR(n)
    for i in range(n):
        f = 1
        tmp = [7, 7, 5, 7, 5]
        for j in range(i, n):
            if tmp[-1] >= len(w[j]):
                tmp[-1] -= len(w[j])
            else:
                f = 0
                break
            if tmp[-1] == 0:
                tmp.pop()
                if tmp:
                    continue
                f = 1
                break
        if f:
            print(i + 1)
            break

    return


#main
if __name__ == '__main__':
    while 1:
        n = II()
        if n == 0:
            break
        solve(n)
