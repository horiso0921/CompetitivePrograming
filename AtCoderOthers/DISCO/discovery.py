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

# A
def A():
    n = II()
    s = S()
    counter = 0
    flg = 0
    ans = [0 for i in range(n)]
    for num,ss in enumerate(s):
        if ss == ">":
            counter += 1
            ans[num] = counter
        else:
            counter = 0
    ansa = 0
    ansb = 0
    counter = 0
    counter_ = 0
    for num,an in enumerate(ans):
        if s[num] == "-":
            if flg == 2:
                flg = 0
                if counter_ > counter:
                    ansa = ansb
                    counter = counter_
                    counter
            elif flg == 1:
                flg += 1
        else:
            if flg == 2:
                counter_ += 1
            elif flg == 1:
                counter_ += 1
            else:
                flg += 1
                counter_ += 1

                
            

    print(ans)

    return

# B
def B():
    return

# C
def C():
    return

# D
def D():
    return

# E
def E():
    return

# F
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
    A()
