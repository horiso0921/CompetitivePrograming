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
    n = II()
    s = SR(n)
    t = SR(n)

    t = [[i,j] for i in range(n) for j in range(n) if t[i][j] == "#"]
    tmi = n
    tmai = 0
    tmj = n
    tmaj = 0
    for i,j in t:
        tmi = min(i,tmi)
        tmai = max(i,tmai)
        tmj = min(j,tmj)
        tmaj = max(j,tmaj)
    for i in range(len(t)):
        t[i][0] -= tmi
        t[i][1] -= tmj
    t.sort()
    lti = tmai - tmi
    ltj = tmaj - tmj

    s = [[i,j] for i in range(n) for j in range(n) if s[i][j] == "#"]
    smi = n
    smai = 0
    smj = n
    smaj = 0
    for i,j in s:
        smi = min(i,smi)
        smj = min(j,smj)
        smai = max(i,smai)
        smaj = max(j,smaj)
    for i in range(len(s)):
        s[i][0] -= smi
        s[i][1] -= smj
    s.sort()
    lsi = smai - smi
    lsj = smaj - smj
    for _ in range(4):
        tmp = []
        for i,j in s:
            tmp.append([i,j])
        tmp.sort()
        if tmp == t:
            print("Yes")
            return
        s = []
        for i,j in tmp:
            ii = i - lsi / 2
            jj = j - lsj / 2
            ni = jj + lsj / 2
            nj = - ii + lsi / 2
            ni = int(ni)
            nj = int(nj)
            s.append([ni, nj])
        lsi, lsj = lsj, lsi
    print("No")
    return
 

#main
if __name__ == '__main__':
    solve()