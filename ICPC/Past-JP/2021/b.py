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
def solve(w,h):
    xyn = LIR(w+h-1)
    dx = defaultdict(list)
    dy = defaultdict(list)
    for x,y,n in xyn:
        dx[x].append((y,n))
        dy[y].append((x,n))
    xx = [None] * (w+1)
    yy = [None] * (h+1)
    q = deque()
    checkx = defaultdict(int)
    checky = defaultdict(int)
    xx[1] = 0
    for i,n in dx[1]:
        q.append((1,i))
        checky[i] = 1
        yy[i] = n 

    while q:
        x,y = q.popleft()
        for i,n in dx[x]:
            if yy[i] == None:
                yy[i] = n - xx[x]
                q.append((x,i))
            else:
                if yy[i] == n - xx[x]:
                    continue
                else:
                    print("NO")
                    return
        for i,n in dy[y]:
            if xx[i] == None:
                xx[i] = n - yy[y]
                q.append((i,y))
            else:
                if xx[i] == n - yy[y]:
                    continue
                else:
                    print("NO")
                    return
            
    for i in range(1,w+1):
        if xx[i] != None: continue
        print("NO")
        return
    for i in range(1,h+1):
        if yy[i] != None: continue
        print("NO")
        return
    print("YES")

    return


#main
if __name__ == '__main__':
    while 1:
        
        w, h = LI()
        if w == h == 0: break
        solve(w,h)
    