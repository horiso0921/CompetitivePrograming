
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
# 解説AC
# iが必要←→iを使わずに[k-ai,k)内の和を作れるかの累積和(O(nk))
# 必要性は単調性を満たす(iが必要→jも必要(aj>ai))ので二部探索(O(logn))
def D():
    n, k = LI()
    a = LI()
    a.sort()
    ok = n
    ng = -1
    def f(x):
        dp = [False] * (k)
        dp[0] = True
        kx = k - a[x]
        for i in range(n):
            if i == x: continue
            ai = a[i]
            for j in range(k - 1, ai - 1, -1):
                if dp[j - ai]:
                    dp[j] = True
                    if kx <= j:
                        return True
        for j in range(max(0, k - a[x]), k):
            if dp[j]:
                return True
        return False
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    print(ng + 1)
    return

