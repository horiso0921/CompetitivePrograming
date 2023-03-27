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
    for i in range(II()):
        n,p = LI()
        x = LIR(n)
        print(f"Case #{i+1}: ", end="")
        if 2 <= n <= 10:
            if 2 <= p <= 3:
                
                dp = [[inf] * p for i in range(n+1)]
                dp[0] = [0] * p
                
                x = [[0] * p] + x
                
                for i in range(n):
                    xi = x[i]
                    xi1 = x[i+1]
                    for pj in range(p):
                        dpj = dp[i][pj]
                        for f in itertools.permutations(range(p),p):
                            pre = xi[pj]
                            tmp = 0
                            for pi in f:
                                tmp += abs(pre - xi1[pi])
                                pre = xi1[pi]
                            dp[i+1][pi] = min(dp[i+1][pi], tmp + dpj)
                # print(dp)
                print(min(dp[-1]))
                
            
    return


#main
if __name__ == '__main__':
    solve()