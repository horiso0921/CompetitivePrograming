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
inf = float("INF")

#solve
def solve():
    n = II()
    xy = LIR(n)
    def f(mid):
        q = deque()
        check = defaultdict(int)
        for x,y in xy:
            if y + 100 < mid:
                q.append((x,y))
                check[(x,y)] = 1
        while q:
            x,y = q.pop()
            for mx, my in xy:
                if x != mx or my != y:
                    if (mx - x) ** 2 + (my - y) ** 2 < mid ** 2:
                        if not check[(mx, my)]:
                            q.appendleft((mx, my))
                            check[(mx, my)] = 1
        for key in check.keys():
            x, y = key
            if 100 - y < mid:
                return False
        return True
                        
    ok = 0
    ng = 200
    while ng - ok > 0.0001:
        mid = (ok + ng) / 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    print(ok / 2)
    
    
            
    return
                
        


#main
if __name__ == '__main__':
    solve()
