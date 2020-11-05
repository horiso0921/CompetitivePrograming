#!/usr/bin/env python3
from heapq import heappush, heappop
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
inf = 10 ** 20

#solve
def solve():
    n,m,s,g = LI()
    s-=1
    g-=1
    edg = [[] for i in range(n)]
    for _ in range(m):
        u,v,a,b = LI()
        u-=1
        v-=1
        edg[u].append((v,a,b))
        edg[v].append((u,a,b))
    dist = [inf] * n
    dist[0] = 0
    q = [(0, s)]

    def f(x,a,b):
        return x + (b / (a + x))
    def tf(x,a,b):
        return x + (b - 1) // (a + x) + 1
        
    def bi(x,a,b):
        ok = x
        ng = max(x + 1, b + 1)
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if f(mid, a, b) < f(mid + 1, a, b):
                ng = mid
            else:
                ok = mid
        ok = tf(ok, a, b) 
        ng = tf(ng, a, b)    
        if ok < ng:
            return ok
        else:
            return ng
    while q:
        score, point = heappop(q)
        if dist[point] < score: continue
        for nex, a, b in edg[point]:
            t = bi(score, a, b)
            if t < dist[nex]:
                dist[nex] = t
                heappush(q, (t, nex))
    if dist[g] == inf:
        print(-1)
    else:
        print(dist[g])  
    return


#main
if __name__ == '__main__':
  solve()