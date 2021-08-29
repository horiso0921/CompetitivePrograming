#!/usr/bin/env python3
import sys, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
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
mod = 998244353
inf = 1e10


#solve
def solve():
    n = II()
    a = LI()
    b = LI()
    ab = list(zip(a,b))
    ab.sort()
    N = 5001
    dp = [0] * N
    ans = 0
    dp[0] = 1
    for a,b in ab:
        for i in range(a - b + 1):
            ans += dp[i]
            ans %= mod
        for i in range(N-b-1, -1, -1):
            dp[i + b] += dp[i]
            dp[i + b] %= mod
    print(ans)


            

    return


#main
if __name__ == '__main__':
    solve()