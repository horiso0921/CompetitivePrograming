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
    a, b, c = LI()
    dp = [[[0] * 101 for i in range(101)] for j in range(101)]
    dp[a][b][c] = 1
    for ai in range(a, 100):
        for bi in range(b, 100):
            for ci in range(c, 100):
                d = dp[ai][bi][ci]
                dp[ai + 1][bi][ci] += d * ai / (ai + bi + ci)
                dp[ai][bi + 1][ci] += d * bi / (ai + bi + ci)
                dp[ai][bi][ci + 1] += d * ci / (ai + bi + ci)
                
    ans = 0
    for ai in range(101):
        for bi in range(101):
            for ci in range(101):
                if ai == 100 or bi == 100 or ci == 100:
                    ans += dp[ai][bi][ci] * (ai + bi + ci - a - b - c)
    print(ans)
    return

# main
if __name__ == '__main__':
    solve()
