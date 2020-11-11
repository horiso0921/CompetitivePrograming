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
    x = LI()
    X = defaultdict(int)
    X["AB"] = x[0]
    X["AC"] = x[1]
    X["BC"] = x[2]
    X["BA"] = x[0]
    X["CA"] = x[1]
    X["CB"] = x[2]
    s = S()
    edg = [[] for i in range(n)]
    for _ in range(m):
          a,b,c = LI()
          a-=1
          b-=1
          edg[a].append((b,c))
          edg[b].append((a,c))
    dist = [inf] * n
    q = [(0,0)]
    dist[0] = 0
    cdis = defaultdict(lambda: inf)
    cdis[s[0]] = 0
    clist = defaultdict(list)
    while q:
          score, p = heappop(q)
          if dist[p] < score:
                continue
          for e, c in edg[p]:
                if dist[e] > score + c:
                      cdis[s[e]] = min(cdis[s[e]], score + c)
                      dist[e] = score + c
                      heappush(q, (score + c, e))
    clis = defaultdict(list)
    for i in range(n):
          clist[s[i]].append(dist[i])
          clis[s[i]].append(i)
    clist["A"].sort()
    clist["B"].sort()
    clist["C"].sort()
    rdist = [inf] * n
    q = [(0,n-1)]
    rcdis = defaultdict(lambda: inf)
    rdist[n-1] = 0
    rcdis[s[n-1]] = 0
    while q:
          score, p = heappop(q)
          if rdist[p] < score:
                continue
          for e, c in edg[p]:
                if rdist[e] > score + c:
                      rcdis[s[e]] = min(rcdis[s[e]], score + c)
                      rdist[e] = score + c
                      heappush(q, (score + c, e)) 
    ans = dist[n-1]
    if s[0] != s[n-1]:
          ans = min(ans, X[s[0]+s[n-1]])
    else:
          for c1 in set(s):
                for c2 in set(s):
                      tt = inf
                      if c1 != s[0] and c2 != s[n-1] and c1 != c2:
                            CCdist = [inf] * n
                            q = []
                            for cl in clis[c1]:
                                  heappush(q,(0,cl))
                                  CCdist[cl] = 0
                            while q:
                                  score, p = heappop(q)
                                  if CCdist[p] < score:
                                        continue
                                  for e, c in edg[p]:
                                        if CCdist[e] > score + c:
                                              CCdist[e] = score + c
                                              heappush(q, (score + c, e))
                            for cl in clis[c2]:
                                  tt = min(tt, CCdist[cl]) 
                      if tt != inf:
                            ans = min(ans, tt + X[s[0]+c1] + X[s[n-1]+c2])
                                  
    for c1 in set(s):
        if s[0] != c1 and s[n-1] != c1:
              ans = min(ans, X[s[0]+c1] + X[c1+s[n-1]])
        if s[0] != c1:
          ans = min(ans, rcdis[c1] + X[s[0] + c1])
        if s[n-1] != c1:
          ans = min(ans, cdis[c1] + X[s[n-1] + c1])
        for c2 in set(s):
          if c1 != c2:
            ans = min(ans, cdis[c1] + rcdis[c2] + X[c1+c2])
          if s[0] != c1 and s[n-1] != c2 and c1 != c2:
            ans = min(ans, X[s[0]+c1] + X[c1+c2] + X[c2+s[n-1]])
          if s[0] != c1 and s[n-1] != c1 and c1 != c2:
            ans = min(ans, cdis[c1] + rcdis[c1] + 2 * X[c1+c2])
                
    print(ans) 
#main
if __name__ == '__main__':
    solve()
