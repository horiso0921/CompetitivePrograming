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
    n, k = LS()
    k = int(k)
    dp = [[0] * 17 for i in range(len(n))]
    tmp = set(n[0])
    if "A" <= n[0] <= "F":
        dp[0][1] = 9 + ord(n[0]) - ord("A")
    else:
        dp[0][1] = int(n[0]) - 1
    for i in range(1, len(n)):
        for j in range(16):
            dp[i][j] = (dp[i][j] + dp[i - 1][j] * j) % mod
            dp[i][j + 1] = (dp[i][j + 1] + dp[i - 1][j] * (16 - j)) % mod
        dp[i][16] = (dp[i][16] + dp[i - 1][16] * 16) % mod
        dp[i][1] += 15
        if "A" <= n[i] <= "F":
            for x in range(10):
                if str(x) in tmp: 
                    dp[i][len(tmp)] += 1
                else: 
                    dp[i][len(tmp) + 1] += 1
            for x in ["A", "B", "C", "D", "E", "F"]:
                if x >= n[i]: continue
                if x in tmp: 
                    dp[i][len(tmp)] += 1
                else: 
                    dp[i][len(tmp) + 1] += 1
        else:
            for x in range(10):
                if str(x) >= n[i]: continue
                if str(x) in tmp: 
                    dp[i][len(tmp)] += 1
                else: 
                    dp[i][len(tmp) + 1] += 1
        tmp.add(n[i])
    print((dp[-1][k] + (len(tmp) == k)) % mod)
    return


# main
if __name__ == '__main__':
    solve()
