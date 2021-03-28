from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
mod = 1000000007
inf = float("inf")
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

# solve
def solve():
    n = II()
    xc = LIR(n)
    xc.sort()
    lc = [[] for i in range(n)]
    for i in range(n):
        x, c = xc[i]
        lc[c - 1].append(x)
    dp = defaultdict(lambda: inf)
    dp[0] = 0
    for i in range(n):
        if lc[i] == []: continue
        dp1 = defaultdict(lambda: inf)
        l, r = lc[i][0], lc[i][-1]
        if l == r:
            for k, v in dp.items():
                dp1[l] = min(dp1[l], v + abs(k - l))
        else:
            for k, v in dp.items():
                if l <= k <= r:
                    dp1[l] = min(dp1[l], v + abs(k - r) + abs(l - r))
                    dp1[r] = min(dp1[r], v + abs(k - l) + abs(l - r))
                else:
                    if k <= l:
                        dp1[r] = min(dp1[r], v + abs(k - r))
                    else:
                        dp1[l] = min(dp1[l], v + abs(k - l))
        dp = dp1
    ans = inf
    for k, v in dp.items():
        ans = min(ans, abs(k) + v)
    print(ans)
    return


# main
if __name__ == '__main__':
    solve()
