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
mod = 998244353
inf = 1e10

#solve
def solve():
    n = II()
    s = S()
    M = 1 << 10
    dp = [[0] * 10 for i in range(1 << 10)]
    for i in range(n):
        dp2 = [[0] * 10 for i in range(1 << 10)]
        si = ord(s[i]) - ord("A")
        
        dp2[0][si] = 1
        xx = 1 << si
        for mask in range(M):
            if mask & xx:
                for j in range(10):
                    if (1 << j) & mask:
                        continue
                    dp2[mask][j] += dp[mask][j]
                    dp2[mask][j] %= mod
            else:
                for j in range(10):
                    if (1 << j) & mask:
                        continue
                    if si != j:
                        dp2[mask | (1 << j)][si] += dp[mask][j]  # 追加した場合
                        dp2[mask | (1 << j)][si] %= mod
                        dp2[mask][j] += dp[mask][j] # 追加しなかった場合
                        dp2[mask][j] %= mod
                    else:
                        dp2[mask][si] += dp[mask][si] * 2 # 追加しなかった場合 と した場合
                        dp2[mask][si] %= mod

        dp = dp2
    ans = 0
    for di in dp:
        for d in di:
            ans += d
            ans %= mod
    print(ans)
                    


    return


#main
if __name__ == '__main__':
    solve()