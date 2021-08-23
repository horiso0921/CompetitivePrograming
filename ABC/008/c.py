
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
import math
fact = [math.factorial(n) for n in range(101)]
n = int(input())
c = [int(input()) for i in range(n)]
yakusu = [-1 for i in range(n)]
for i in range(n):
    for k in range(n):
        if c[i] % c[k] == 0:
            yakusu[i] += 1
ans = 0
omote = [0 for i in range(n)]
for i in range(n):
    for k in range(i // 2 + 1):
        omote[i] += fact[n] / fact[i + 1] / fact[n - i - 1] * fact[n - i - 1] * fact[i] 
for i in yakusu:
    ans += omote[i]
print(ans / fact[n])


