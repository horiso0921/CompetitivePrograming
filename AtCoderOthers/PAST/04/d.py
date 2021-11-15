#!/usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys
import itertools
import math
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
    n = II()
    s = list(S())
    x = 0
    y = 0
    while "." in s:
        l,r = 0,0
        for li in range(n-1):
            if s[li+1] == "#" and s[li] == ".":
                l += 1
        for ri in range(n-1):
            if s[ri] == "#" and s[ri+1] == ".":
                r += 1
        if l > r:
            x += 1
            for li in range(n-1):
                if s[li+1] == "#" and s[li] == ".":
                    s[li] = "#"
        else:
            y += 1
            for ri in range(n-1)[::-1]:
                if s[ri] == "#" and s[ri+1] == ".":
                    s[ri+1] = "#"
    print(x, y)


#main
if __name__ == '__main__':
  solve()
