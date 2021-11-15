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


mod = 1000000000
inf = float('INF')

#solve


def solve():
    n,q = LI()
    h = LI()
    ans = defaultdict(int)
    lis = [None] * (n-1)
    for i in range(n-1):
        tmp = h[i] - h[i+1]
        tmp *= -1 if i & 1 else 1
        ans[tmp] += 1
        lis[i] = tmp
    odd = 0
    even = 0
    for _ in range(q):
        q = LS()
        if q[0] == "1":
            _, v = q
            v = int(v)
            odd += v
        elif q[0] == "2":
            _, v = q
            v = int(v)
            even += v
        else:
            _, u, v = q
            u, v = int(u), int(v)
            u-=1
            f = u & 1
            for _ in range(2):
                if 0 <= u < (n - 1):
                    ans[lis[u]] -= 1
                    if f:
                        lis[u] -= v
                    else:
                        lis[u] += v
                    ans[lis[u]] += 1
                u -= 1
        print(ans[even - odd])
    return
                
            
                
#main
if __name__ == '__main__':
    solve()
