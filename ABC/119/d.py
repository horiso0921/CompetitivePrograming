
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
a, b, q = map(int, input().split())
s = [int(input()) for i in range(a)]
t = [int(input()) for i in range(b)]
s.sort()
t.sort()

import bisect


for i in range(q):
    x = int(input())
    s_l = bisect.bisect_left(s, x) - 1
    t_l = bisect.bisect_left(t, x) - 1
    s_r = s_l + 1
    t_r = t_l + 1
    if s_l == -1:
        s_l = 0
    if t_l == -1:
        t_l = 0
    if s_l == a :
        s_l = a - 1
        s_r = a - 1
    if s_r == a:
        s_r = a - 1
    if t_l == b:
        t_l = b - 1
        t_r = b - 1
    if t_r == b:
        t_r = b - 1
    ans = min(abs(t[t_l] - s[s_r]) + min(abs(t[t_l] - x), abs(s[s_r] - x)),
    abs(s[s_l] - t[t_r]) + min(abs(s[s_l] - x), abs(t[t_r] - x)),
    abs(s[s_l] - t[t_l]) + min(abs(s[s_l] - x), abs(t[t_l] - x)),
    abs(s[s_r] - t[t_r]) + min(abs(s[s_r] - x), abs(t[t_r] - x)),
    )
    
    print(ans)

