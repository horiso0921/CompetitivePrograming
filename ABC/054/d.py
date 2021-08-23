
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
    n, Ma, Mb = LI()
    abc = LIR(n)
    dp = [[inf] * (10 * n + 1) for i in range(10 * n + 1)]
    dp[0][0] = 0
    for a, b, c in abc:
        for i in range(10 * n, a - 1, -1):
            for j in range(10 * n, b - 1, -1):
                dp[i][j] = min(dp[i - a][j - b] + c, dp[i][j])
    ans = inf
    ma = Ma
    mb = Mb
    i = 1
    while 1:
        ans = min(ans, dp[ma * i][mb * i])
        i += 1
        if ma * i > 10 * n or mb * i > 10 * n:
            break
    if ans == inf:
        print(-1)
        return
    
    print(ans)
    return

