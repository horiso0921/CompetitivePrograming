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
    n = II() * 3
    s = S()
    dp = [[0] * n for i in range(3)]
    a_dp = [[] for i in range(3)]

    for i in range(n):
        x = ord(s[i]) - ord("A")
        dp[x][i] = 1
    
    for i in range(3):
        a_dp[i] = list(itertools.accumulate([0]+dp[i]))
    
    print(a_dp)
    ans = [0] * n
    for patterns in itertools.permutations(range(3), 3):
        for p in patterns:
            p0 = p[0]
            p1 = p[1]
            p2 = p[2]
            init = 0
            l = 0
            r = n + 1
            while r - l > 1:
                m = (r + l) // 2
                if a_dp[m][p0] < 

    return


#main
if __name__ == '__main__':
    solve()