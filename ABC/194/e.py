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
    n, m = LI()
    dp = [[-1] for i in range(n + 1)]
    a = LI()
    for i in range(n):
        dp[a[i]].append(i)
    for i in range(n + 1):
        dp[i].append(n)

    for i in range(n + 1):
        for j in range(len(dp[i]) - 1):
            x, y = dp[i][j], dp[i][j + 1]
            if y - x > m:
                print(i)
                return
    return


# main
if __name__ == '__main__':
    solve()
