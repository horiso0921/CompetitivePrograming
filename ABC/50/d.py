
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
    n = II()
    binmax = len(bin(n)) - 2
    dp = [[0] * 3 for i in range(binmax + 1)]
    dp[0][0] = 1
    for i in range(binmax):
        if (n >> binmax - i - 1) & 1:
            # nについて2進数のとき左からibit目が立つ

            # 前bit迄決めた時の和の差が0で今回bitが立つため
            # a,bのここのbitどちらかを立たせると和の差が0
            dp[i + 1][0] = dp[i][0] % mod

            # 前bitを決めた時の和の差が0で今回bitが立つため
            # a,bのここのbitを0にすると和の差が1 dp[i][0]
            # 前bitを決めた時の和の差が1で今回bitが立つため
            # この時点での和の差が3あるため
            # a,bのここのbitを1にすると和の差が1 dp[i][1]
            dp[i + 1][1] = (dp[i][0] + dp[i][1]) % mod

            # 前bitを決めた時の和の差が1で今回bitが立つため
            # この時点での和の差が3あるため
            # a,bのここのbitを(0,1),(0,0)にすると和の差が2以上
            # (0,1)と(1,0)は同じものなので dp[i][1]
            # 前bitを決めた時の和の差が2以上で今回bitが立つため
            # この時点での和の差が4以上あるため
            # 何をしても差は2以上で3通り dp[i][2]
            dp[i + 1][2] = (2 * dp[i][1] + 3 * dp[i][2]) % mod
        else:
            # nについて2進数のとき左からibit目が立たない

            # 前bit迄決めた時の和の差が0で今回bitが立たないため
            # a,bのここのbitを立たせないと和の差が0 dp[i][0]
            # 前bit迄決めた時の和の差が1で今回bitが立たないため
            # この時点での和の差が2あるため
            # a,bのここのbitを立たせると和の差が0 dp[i][1]
            dp[i + 1][0] = (dp[i][0] + dp[i][1]) % mod

            # 前bit迄決めた時の和の差が1で今回bitが立たないため
            # この時点での和の差が2あるため
            # a,bのここのbitをどちらかを立たせると和の差が1 dp[i][1]
            dp[i + 1][1] = dp[i][1] % mod

            # 前bitを決めた時の和の差が1で今回bitが立たないため
            # この時点での和の差が2あるため
            # a,bのここのbitを(0,0)にすると和の差が2以上 dp[i][1]
            # 前bitを決めた時の和の差が2以上で今回bitが立たないため
            # この時点での和の差が4以上あるため
            # 何をしても差は2以上で3通り dp[i][2]
            dp[i + 1][2] = (dp[i][1] + 3 * dp[i][2]) % mod

    print(sum(dp[-1]) % mod)

    return


