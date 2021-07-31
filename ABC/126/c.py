
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
def C():
    n, k = LI()
    ans = 0
    if k == 1:
        print(1)
        return
    nibuiti = [None for i in range(int(math.log2(k) + 1))]
    for num in range(int(math.log2(k) + 1)):
        if num == 0:
            nibuiti[num] = 1 / 2
            continue
        nibuiti[num] = nibuiti[num-1]/2
        
    for i in range(1, n + 1):
        if i >= k:
            ans += 1
            continue
        b = nibuiti[int(math.log2((k - 1) // i))]
        ans += b
    print(ans/n)
    return

