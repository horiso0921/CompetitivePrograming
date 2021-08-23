
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
    def check(n):
        ans = 0
        n = int("".join(map(str, n)))
        for i in range(1,n+1):
            if "1" in str(i):
                ans += str(i).count("1")
        print(ans)
    n = list(map(int, S()))
    if n == -1:
        n = II()
        check(n)
    dp = [[0] * 10 for i in range(10)]
    for i in range(1,10):
        for j in range(10):
            if j == 2:
                dp[i][j] = 10 ** (i - 1)
            for k in range(10):
                dp[i][j] += dp[i - 1][k]
    ans = 0
    for num, ni in enumerate(n[::-1]):
        ans += sum(dp[num + 1][1:ni + 1])
        if ni == 1:
            if num == 0:
                ans += 1
            else:
                ans += int("".join(map(str, n[-num:]))) + 1
    print(ans)
    return

