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
    n,m,k = LI()
    s = SR(n)
    ans = 0
    for y in range(n):
        for x in range(m):
            for N in range(1,31):
                if x + N > m or y + N > n: break
                for i in range(10):
                    tmp = 0
                    i = str(i)
                    for mx in range(x, x+N):
                        for my in range(y, y+N):
                            if s[my][mx] != i:
                                tmp += 1
                    if tmp > k:
                        continue
                    ans = max(ans, N)
    print(ans)


#main
if __name__ == '__main__':
    solve()
