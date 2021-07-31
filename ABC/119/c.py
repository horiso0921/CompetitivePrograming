
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
import itertools

n, a, b, c = map(int, input().split())
abc = [a, b, c]
ans = float("INF")
x = [int(input()) for i in range(n)]
nums = list(itertools.product([0, 1, 2, 3], repeat = n))
#print(nums)
for i in nums:
    tmp = 0
    aa = 0
    ba = 0
    ca = 0
    for number, k in enumerate(i):
        if k == 1:
            if aa != 0:
                tmp += 10
            aa += x[number]
        if k == 2:
            if ba != 0:
                tmp += 10
            ba += x[number]
        if k == 3:
            if ca != 0:
                tmp += 10
            ca += x[number]
    if aa == 0 or ba == 0 or ca == 0:
        tmp = float("INF")
    else:
        tmp += abs(aa - a)
        tmp += abs(ba - b)
        tmp += abs(ca - c)
    ans = min(tmp, ans)
print(ans)
        
        
            


