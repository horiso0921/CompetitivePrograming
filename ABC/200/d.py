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
    a = [i % 200 for i in LI()]
    revdp = [[[]] * 200 for i in range(n + 1)]
    for i in range(n - 1, 0, -1):
        dpi1 = revdp[i - 1]
        dpi = revdp[i]
        dpi1[a[i]] = [i + 1]
        for j in range(200):
            if dpi[j]:
                dpi1[(j + a[i]) % 200] =  [i + 1] + dpi[j]
                dpi1[j] = dpi[j]
    dp = [[[[] for _ in range(200)] for j in range(i + 2)] for i in range(n)]
    dp[0][1][a[0]] = [1]
    if revdp[0][0]:
        print("Yes")
        print(1, 1)
        print(1 + len(revdp[0][0]), 1, *revdp[0][0])
        return
    for i in range(1, n):
        klis = defaultdict(set)
        for j in range(1, i+1):
            for k in range(200):
                if dp[i - 1][j][k]:
                    dp[i][j][k] = dp[i - 1][j][k]
                    klis[k].add(j)
        if dp[i][1][a[i]]:
            print("Yes")
            print(1, *dp[i][1][a[i]])
            print(1, i + 1)
            return
        dp[i][1][a[i]] = [i + 1]
        for j in range(1, i + 2):
            for k in range(200):
                if dp[i - 1][j - 1][k]:
                    if klis[(k + a[i]) % 200]:
                        for kk in klis[(k + a[i]) % 200]:
                            print("Yes")
                            print(kk, *dp[i][kk][(k + a[i]) % 200])
                            print(j, *dp[i-1][j - 1][k], i + 1)
                            return
                    dp[i][j][(k + a[i]) % 200] = dp[i - 1][j - 1][k] + [i + 1]
    print("No")
    return


#main
if __name__ == '__main__':
    solve()