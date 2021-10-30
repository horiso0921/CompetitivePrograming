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
    a = LI()
    aa = list(itertools.accumulate(a))
    b = LI()
    bb = list(itertools.accumulate(b))
    dp = [[[0]* for j in range(m+1)] for i in range(n+1)]
    dp[n][m][0] = 0
    dp[n][m][1] = 0
    for i in range(n,-1,-1):
        for j in range(m,-1,-1):
            print(i,j,dp)
            tmp = 0
            cana = 0
            canb = 0
            if i != 0 or j != 0 or 1:
                for ii in range(i, n):
                    if a[ii] == -1:
                        canb = 0
                    else:
                        cana += a[ii]
                    if j == m:
                        tmp = max(tmp, dp[ii+1][j][0] + cana - canb)
                    for jj in range(j, m):
                        tmp1 = dp[ii+1][j][0] + cana - canb
                        if b[jj] == -1:
                            cana = 0
                        else:
                            canb += b[jj]
                        tmp2 = dp[ii+1][jj+1][1] + cana - canb
                        tmp = max(tmp, min(tmp1, tmp2))

                    print(tmp)
                dp[i][j][0] = tmp                

            tmp = 0
            cana = 0
            canb = 0
            for jj in range(j, m):
                if b[jj] == -1:
                    cana = 0
                else:
                    canb += b[jj]
                if i == n:
                    tmp = min(tmp, dp[i][jj+1][1] + cana - canb)
                for ii in range(i, n):
                    tmp1 = dp[ii][jj+1][1] + cana - canb
                    if a[ii] == -1:
                        canb = 0
                    else:
                        cana += a[ii]
                    tmp2 = dp[ii+1][jj+1][0] + cana - canb
                    tmp = min(tmp, max(tmp1, tmp2))
                    print(cana,canb)
                print(tmp)
            dp[i][j][1] = tmp
    for di in dp:
        print(di)
    return


#main
if __name__ == '__main__':
    solve()