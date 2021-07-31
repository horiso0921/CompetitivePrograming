
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
n,m = map(int, input().split())
a = list(map(int, input().split()))
num = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
ans = [-float("inf") for _ in range(n + 1)]
num_ans = []
a.sort(reverse=True)
for i in a:
    num_ans.append(num[i])
ans[0] = 0
for i in range(n + 1):
    for b in num_ans:
        if i - b >= 0:
            ans[i] = max(ans[i - b] + 1, ans[i])
anse = ""
while ans[n] > 0:
    for k, i in enumerate(num_ans):
        if n - i >= 0:
            
            if ans[n] - 1 == ans[n - i]:
                anse += str(a[k])
                n -= i
                break
    if n < 0:
        break
            
print(anse)