
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
n, K = map(int, input().split())
s = list(input())
sb = sorted(s)
ans = []
def hantei(i, k, sb):
    ansnum = 0
    a = s[i:n]
    b = sb[::1]
    if a[0] != k:
        ansnum += 1
    del a[0]
    b.remove(k)
    for j in set(a):
        if a.count(j) > b.count(j):
            ansnum += a.count(j) - b.count(j)
    return ansnum
ansn = 0
for i in range(n):
    for k in sb:
        ansnumb = hantei(i, k, sb)
        if ansnumb + ansn <= K:
            if s[i] != k:
                ansn += 1
            sb.remove(k)
            ans.append(k)
            break

for i in ans: print(i, end="")
print()


