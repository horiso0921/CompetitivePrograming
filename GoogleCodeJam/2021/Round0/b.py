from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
mod = 1000000007
inf = 1e20
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
    t = II()
    cj = {"C":0, "J":1}
    for t in range(1, t + 1):
        x, y, s = LS()
        x, y = int(x), int(y)
        dp = [[inf] * 2 for i in range(len(s))]
        if s[0] == "?":
            dp[0][0] = 0
            dp[0][1] = 0
        else:
            dp[0][cj[s[0]]] = 0
        for i in range(1, len(s)):
            if s[i] == "?":
                dp[i][0] = min(dp[i - 1][0], dp[i - 1][1] + y)
                dp[i][1] = min(dp[i - 1][0] + x, dp[i - 1][1])
            else:
                if s[i] == "C":
                    dp[i][0] = min(dp[i - 1][0], dp[i - 1][1] + y)
                else:
                    dp[i][1] = min(dp[i - 1][0] + x, dp[i - 1][1])
        print("Case #{}: {}".format(t, min(dp[-1])))
    return


# main
if __name__ == '__main__':
    solve()