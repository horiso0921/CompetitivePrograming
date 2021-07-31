
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
    x, y, z, K = LI()
    a = LI()
    a.sort(reverse=True)
    b = LI()
    b.sort(reverse = True)
    c = LI()
    c.sort(reverse=True)
    ab = []
    for a_ in a:
        for b_ in b:
            ab.append(a_ + b_)
    ab.sort(reverse = True)
    ab = ab[:min(x * y, K)]
    ans = []
    for ab_ in ab:
        for c_ in c:
            ans.append(ab_ + c_)
    ans.sort(reverse = True)
    for k in range(K):
        print(ans[k])



        
                    

    return

