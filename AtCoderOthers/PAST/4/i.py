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
    n = II()
    a = LI()
    a = a + a
    Y = sum(a)//2
    X = 0
    for i in range(n):
        if abs(X+a[i]-(Y-a[i])) < abs(X-Y):
            X += a[i]
            Y -= a[i]
        else:
            break
    ans = abs(X-Y)
    for j in range(n):
        X -= a[j]
        Y += a[j]
        for i in range(i, n+j):
            if abs(X+a[i]-(Y-a[i])) < abs(X-Y):
                X += a[i]
                Y -= a[i]
            else:
                break
        else:
            i += 1
        ans = min(ans, abs(X-Y))
    print(ans)
        

#main
if __name__ == '__main__':
    solve()
