
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
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#solve
def D():
    n, m = LI()
    p = LI_()
    xy = LIR_(m)
    size = [1 for _ in range(n)]
    height = [1 for _ in range(n)]
    par = [i for i in range(n)]
    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    def union(x, y):
        s1 = find(x)
        s2 = find(y)
        if s1 != s2:
            if height[s1] < height[s2]:
                par[s1] = s2
                size[s2] += size[s1]
                size[s1] = 0
            else:
                par[s2] = s1
                size[s1] += size[s2]
                size[s2] = 0
                if height[s1] == height[s2]:
                    height[s1] += 1

    for x,y in xy:
        union(x, y)
    ans = 0
    for i in range(n):
        if find(p[i]) == find(i):
            ans += 1
    
    print(ans)
    return

