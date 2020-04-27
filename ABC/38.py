#!/usr/bin/env python3
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
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
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
    s = S()
    if s[-1] == "T":
        print("YES")
    else:
        print("NO")
    return

#B
def B():
    hw1 = LI()
    hw2 = LI()
    for i in range(2):
        for k in range(2):
            if hw1[i] == hw2[k]:
                print("YES")
                return
    print("NO")
    return

#C
def C():
    n = II()
    a = LI()
    x = 1
    ans = 0
    for i in range(n-1):
        if a[i + 1] > a[i]:
            x += 1
        else:
            ans += x * (x + 1) // 2
            x = 1
    ans += x * (x+1)//2
    print(ans)
        
    return

# D
# 解説AC
# DPなんなー
# BITなるものがあるらしい
def D():
    n = II()
    wh = LIR(n)
    wh.sort()
    print(wh)
    dp = [inf for _ in range(n+1)]
    for _, h in wh:
        i = bisect_left(dp, h)
        dp[i] = h
    print(bisect_left(dp, inf))
    return


#Solve
if __name__ == '__main__':
    D()
