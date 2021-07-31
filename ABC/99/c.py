
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
    n = II()
    dp = [inf for i in range(n + 1)]
    ans = [1]
    x = 6
    while x <= n:
        ans.append(x)
        x = x * 6
    x = 9
    while x <= n:
        ans.append(x)
        x = x * 9
    ans.sort()
    for i in ans:
        dp[i] = 1
    for i in range(1, n + 1):
        if not i in ans:
            a = bisect.bisect_left(ans, i)
            for k in range(a):
                dp[i] = min(dp[i - ans[k]] + 1, dp[i])
    print(dp[n])
    return

