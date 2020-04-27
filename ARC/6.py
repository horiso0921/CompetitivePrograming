#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import *
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
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
    e = LI()
    b = II()
    l = LI()
    ans = [0, 0, 0, 5, 4, 3, 2]
    ansi = 0
    f = False
    if e == l:
        print(1)
        return
    for i in l:
        if i in e:
            ansi += 1
        if i == b:
            f = True 
    if ansi == 5 and f:
        ansi += 1
    print(ans[ansi])
    return

#B
def B():
    n, l = LI()
    ans = [i for i in range(n)]
    for _ in range(l):
        s = input().rstrip()
        for i in range(n - 1):
            if s[2 * i + 1] == "-":
                ans[i], ans[i + 1] = ans[i + 1], ans[i]
    s = input().rstrip()
    for i in range(n):
        if s[2 * i] == "o":
            print(ans[i]+1)
            return
    return

#C
def C():
    n = II()
    w = IR(n)
    b = inf
    ans = []
    for wi in w:
        for i in range(len(ans)):
            if ans[i] >= wi:
                ans[i] = wi
                break
        else:
            ans.append(wi)
    print(len(ans))
    return

#D
def D():
    return

#Solve
if __name__ == '__main__':
    C()
