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
    s = S()
    t = S()
    dp = [[0] * len(t) for i in range(len(s))]
    
    for i in range(len(t)):
        dp[0][i] = int(s[0] == t[i])
    i = 0
    for j in range(1, len(t)):
        dp[i][j] = max(dp[i][j], dp[i][j-1])
        
    for i in range(1, len(s)):
        for j in range(len(t)):
            dp[i][j] = dp[i-1][j]
        if s[i] == t[0]:
            dp[i][0] = 1
        for j in range(1, len(t)):
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + int(s[i] == t[j]))
        for j in range(1, len(t)):
            dp[i][j] = max(dp[i][j], dp[i][j-1])
    dp = [[0] * len(t)] + dp
    m = max(dp[-1])
    tmp = len(t)
    ans = []
    for i in range(len(s),0,-1):
        if m not in dp[i-1][:tmp]:
            ans.append(t[dp[i][:tmp].index(m)])
            tmp = dp[i][:tmp].index(m)
            m -= 1
            if m == 0:
                break
    print("".join(ans[::-1]))
    return


#main
if __name__ == '__main__':
    solve()