from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
mod = 1000000007
inf = 1e10
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
    h, w, a, b = LI()
    dp = [[0] * (b + 1) for i in range(1 << w)]
    ndp = [[0] * (b + 1) for i in range(1 << w)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            for mask in range(1 << w):
                if mask & 1 << j:
                    for k in range(b + 1):
                        ndp[mask & ~(1 << j)][k] += dp[mask][k]
                else:
                    for k in range(b):
                        ndp[mask][k + 1] += dp[mask][k]
                        if j + 1 < w and not (mask >> (j + 1) & 1):
                            ndp[mask | 1 << (j + 1)][k] += dp[mask][k]
                        if i + 1 < h:
                            ndp[mask | 1 << j][k] += dp[mask][k]
                    if j + 1 < w and not (mask >> (j + 1) & 1):
                        ndp[mask | 1 << (j + 1)][b] += dp[mask][b]
                    if i + 1 < h:
                        ndp[mask | 1 << j][b] += dp[mask][b]

            dp = ndp[:]
            ndp = [[0] * (b + 1) for i in range(1 << w)]
            # print(dp, ndp)
    print(dp[0][-1])

    return


# main
if __name__ == '__main__':
    solve()
