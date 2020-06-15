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
inf = float('INF')

#solve
def solve():
    n = II()
    a = LIR(n - 1)
    def dfs(i, tmp):
        if i == n:
            l = [[] for i in range(3)]
            for i in range(n):
                l[tmp[i]].append(i)
            tmp = 0
            for i in range(3):
                i = l[i]
                for j in range(len(i)):
                    for k in range(j + 1, len(i)):
                        tmp += a[i[j]][i[k] - 1 - i[j]]
            return tmp
        res = -inf
        for j in range(3):
            res = max(res, dfs(i + 1, tmp + [j]))
        return res
    print(dfs(0, []))
    return


#main
if __name__ == '__main__':
    solve()
