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
    n = II()
    cx = LIR(2 * n)
    dp = [0] * (n+1)
    X = [0] * n
    for c,x in cx:
        x -= 1
        if c == "I":
            if x >= 0:
                X[x] += 1
        elif c == "O":
            if x >= 0:
                X[x] += 2
    d = defaultdict(int)
    for i in range(4):
        d[i] = X.count(i)
    time_d = [0] * 3
    for i in range(2 * n):
        ndp = [0] * (n+1)
        c,x = cx[i]
        x -= 1
        in_n = sum(time_d)
        if c == "I":
            if x >= 0:
                if X[x] & 2:
                    time_d[0] += 1
                    for j in range(n+1):
                        ndp[j] += dp[j]
                else:
                    time_d[1] += 1
                    for j in range(n):
                        ndp[j+1] += dp[j]
            else:
                time_d[2] += 1
                no_ketu_no_time_n = d[0]
                ok_ketu_no_time_n = d[2]
                for j in range(n+1):
                    no_ketu_no_time_in = j - time_d[1]
                    if no_ketu_no_time_in > 0:
                        no_ketu_no_time_go = no_ketu_no_time_n - no_ketu_no_time_in
                        if no_ketu_no_time_go > 0:
                            ndp[j+1] += dp[j] * no_ketu_no_time_go
                    
                    ok_ketu_no_time_in = in_n - no_ketu_no_time_in - time_d[0] - time_d[1]
                    if ok_ketu_no_time_in > 0:
                        ok_ketu_no_time_go = ok_ketu_no_time_n - ok_ketu_no_time_in
                        if ok_ketu_no_time_go > 0:
                            ndp[j] += dp[j] * ok_ketu_no_time_go
        
        else:
            if x >= 0:
                if X[x] & 2:
                    time_d[0] -= 1
                    for j in range(n+1):
                        ndp[j] += dp[j]
                else:
                    time_d[1] -= 1
                    for j in range(n):
                        ndp[j+1] += dp[j]
            else:
                time_d[2] -= 1
                no_ketu_no_time_n = d[0]
                ok_ketu_no_time_n = d[2]
                for j in range(n+1):
                    no_ketu_no_time_in = j - time_d[1]
                    if no_ketu_no_time_in > 0:
                        no_ketu_no_time_go = no_ketu_no_time_n - no_ketu_no_time_in
                        if no_ketu_no_time_go > 0:
                            ndp[j+1] += dp[j] * no_ketu_no_time_go
                    
                    ok_ketu_no_time_in = in_n - no_ketu_no_time_in - time_d[0] - time_d[1]
                    if ok_ketu_no_time_in > 0:
                        ok_ketu_no_time_go = ok_ketu_no_time_n - ok_ketu_no_time_in
                        if ok_ketu_no_time_go > 0:
                            ndp[j] += dp[j] * ok_ketu_no_time_go
            
                
                    
                        
                
        
    
                
    return


#main
if __name__ == '__main__':
    solve()