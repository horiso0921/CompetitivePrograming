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
    s = S()
    if s[0] == s[2] and s[1] == s[3]:
        print("Yes")
    else:
        print("No")
    return

# B
def B():
    s = S()
    ans = 1
    ansb = deque()
    for i in range(len(s)-1):
        if s[i] == "2" and s[i + 1] == "5":
            ansb.append(i)
    if not ansb:
        print(-1)
        return
    while ansb:
        i = ansb.pop()
        del s[i + 1]
        del s[i]
    while s:
        flg = 0
        ansb = deque()
        for i in range(len(s)-1):
            if s[i] == "2" and s[i + 1] == "5":
                ansb.append(i)
                flg = 1
        if not flg:
            print(-1)
            return
        while ansb:
            i = ansb.pop()
            del s[i + 1]
            del s[i]
        ans += 1
    print(ans)
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
    B()
