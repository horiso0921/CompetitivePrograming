#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    se = LIR(3)
    ans = 0
    for s, e in se:
        ans += s * (e * 0.1)
    print(int(ans))
    return

#B
def B():
    x = S()
    li = ["o", "k", "u"]
    ch = ["c", "h"]
    flg = 0
    for i in range(len(x)):
        if x[i] in li:
            continue
        if ch[flg] == x[i]:
            flg += 1
            flg = flg % 2
            continue
            
        #print(i)
        print("NO")
        return
    print("YES")
    return

#C
def C():
    n, m = LI()
    dp = [0 for _ in range(m+1)]
    ans = 0
    for _ in range(n):
        l, r, s = LI_()
        ans += s + 1
        dp[l] += s + 1
        dp[r + 1] -= s + 1
    for i in range(m):
        dp[i+1] += dp[i] 
    print(ans-min(dp[:m]))

    return

#D
def D():
    n, m = LI()
    f = IR(n)
    left = [0] * n
    left_f = [0] * (m+1)
    for i in range(n):
        left[i] = max(left[i - 1], left_f[f[i]])
        left_f[f[i]] = i + 1
    dp = [0] * (n + 1)
    dp[0] = 1
    masure = 1
    l = 0
    for i in range(1,n+1):
        for k in range(l,left[i-1]):
            masure -= dp[k]
        l = left[i-1]
        dp[i] += masure
        dp[i] %= mod
        masure += dp[i]
    print(dp[-1])
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    D()
