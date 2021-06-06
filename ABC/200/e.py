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
    n,k = LI()
    dp = [[0] * (3*n + 2) for i in range(4)]
    dp[0][0] = 1
    for i in range(1,4):
        for j in range(2*n+1):
            dp[i][j + 1] += dp[i-1][j]
            dp[i][j + n + 1] -= dp[i-1][j]
        for j in range(1,3*n+1):
            dp[i][j] += dp[i][j-1]
    for i in range(3*n+1):
        if k <= dp[3][i]: 
            x = i
            break
        k -= dp[3][i]
    
    for i in range(1,n+1):
        beauti = i
        amount = x - i
        if amount > 2 * n:
            continue
        umami = n - (amount - n) + 1
        if umami < k:
            k -= umami
        else:
            for j in range(1, n+1):
                if 1 <= x - (i + j) <= n:
                    if k == 1:
                        print(i,j,x-i-j)
                        return
                    k -= 1


    return


#main
if __name__ == '__main__':
    solve()