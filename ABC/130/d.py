
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
    n, k = LI()
    a = LI()
    dp = [0] * (n)
    for i in range(n):
        dp[i] += dp[i - 1] + a[i]
    ans = 0
    def main_bisect(dp):
        dp.insert(0, 0)
        for i in range(1,n+1):
            ai = bisect_left(dp, k + dp[i-1])
            ans += n+1 - ai
        print(ans)
    def main_Measure_method():
        ans = 0
        anssum = 0
        j = 0
        for i in range(n):
            while anssum < k:
                if j == n:
                    break
                else:
                    anssum += a[j]
                    j += 1
            if anssum < k:
                break
            ans += n - j + 1
            anssum -= a[i]
        print(ans)
    main_Measure_method()
    return

