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
    n,m = LI()
    ak = [None] * m
    first = [-1] * n 
    second = []
    for i in range(m):
        _ = II()
        tmp = LI_()
        ak[i] = tmp[::-1]
        f = ak[i][-1]
        if first[f] == -1:
            first[f] = i
        else:
            second.append((first[f], i))
    ans = 0
    while second:
        ans += 2
        i,j = second.pop()
        ak[i].pop()
        ak[j].pop()
        if ak[i]:
            f = ak[i][-1]
            if first[f] == -1:
                first[f] = i
            else:
                second.append((first[f], i))
        if ak[j]:
            f = ak[j][-1]
            if first[f] == -1:
                first[f] = j
            else:
                second.append((first[f], j))
    if ans == 2 * n:
        print("Yes")
    else:
        print("No")        

    return


#main
if __name__ == '__main__':
    solve()