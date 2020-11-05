#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
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
def LIR(n):
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
    N,M = LI()
    # Nが勝つ場合
    # Ｍの攻撃は分散，Nの攻撃は一点集中？
    ans = 0
    n = N * 2
    m = M * 2
    while 1:
        if n < N:
            m -= n
        else:
            m -= N
        if m <= 0:
            break
        ans += 1
        n -= (m + 1) // 2
        if n <= 0:
            break
        ans += 1
    tmp = 0
    n = N * 2
    m = M * 2
    while 1:
        m -= (n + 1) // 2
        if m <= 0:
            break
        tmp += 1
        if m < M:
            n -= m
        else:
            n -= M
        if n <= 0:
            break
        tmp += 1
    print(min(ans, tmp))
    return


#main
if __name__ == '__main__':
  solve()