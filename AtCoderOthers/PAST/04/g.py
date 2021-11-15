#!/usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys
import itertools
import math
from typing import Iterator
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


def IR(n):
  res = [None] * n
  for i in range(n):
    res[i] = II()
  return res


def LIR(n):
  res = [None] * n
  for i in range(n):
    res[i] = LI()
  return res


def FR(n):
  res = [None] * n
  for i in range(n):
    res[i] = IF()
  return res


def LFR(n):
  res = [None] * n
  for i in range(n):
    res[i] = IF()
  return res


def LIR_(n):
  res = [None] * n
  for i in range(n):
    res[i] = LI_()
  return res


def SR(n):
  res = [None] * n
  for i in range(n):
    res[i] = S()
  return res


def LSR(n):
  res = [None] * n
  for i in range(n):
    res[i] = LS()
  return res


mod = 1000000007
inf = float('INF')

#solve


def solve():
    n,m = LI()
    s = SR(n)
    par = [i for i in range(n*m)]
    size = [1]*(n*m)
    def root(x):
        if par[x] == x:
            return x
        par[x] = root(par[x])
        return par[x]
    def unite(x,y):
        x = root(x)
        y = root(y)
        if x == y: return
        if size[x] < size[y]: x,y=y,x
        par[y] = x
        size[x] += size[y]
    for y in range(n):
        for x in range(m):
            if s[y][x] == "#": 
                par[y*m+x] = -1
                continue
            for mx, my in [(0,1),(1,0),(-1,0),(0,-1)]:
                mx += x
                my += y
                if 0 <= mx < m and 0 <= my < n:
                    if s[my][mx] == ".":
                        unite(my*m+mx, y*m+x)
    for y in range(n):
        for x in range(m):
            if s[y][x] == "#": continue 
            root(y*m+x)
    ans = 0
    if len(set(par)) == 2:
        for y in range(n):
            for x in range(m):
                if s[y][x] == "#": 
                    for mx, my in [(0,1),(1,0),(-1,0),(0,-1)]:
                        mx += x
                        my += y
                        if 0 <= mx < m and 0 <= my < n:
                            if s[my][mx] == ".":
                                ans += 1
                                break
    else:
        tmp = set(par)
        for y in range(n):
            for x in range(m):
                if s[y][x] == "#":
                    t = [-1] 
                    for mx, my in [(0,1),(1,0),(-1,0),(0,-1)]:
                        mx += x
                        my += y
                        if 0 <= mx < m and 0 <= my < n:
                            if s[my][mx] == ".":
                                t.append(root(my*m+mx))
                    if tmp == set(t):
                        ans += 1
    print(ans)
        
#main
if __name__ == '__main__':
      solve()
