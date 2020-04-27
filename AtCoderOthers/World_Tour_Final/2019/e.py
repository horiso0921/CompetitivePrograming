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
def S(): return input().rstrip()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10
fc = [1] * 1010
ifc = [1] * 1010
Bn = [0] * 1010

def ad(x, y=0):
    return (x + y) % mod

def mlt(x, y=1):
    return (x * y) % mod
    
def pwr(x, y):
    return pow(x, y, mod)

def inv(x):
    return pwr(x, mod - 2)

def bn(x):
    if x > 0 and Bn[x] == 0: Bn[x] = ad(1, mlt(x, bn(x - 1)))
    return Bn[x]

#solve
def solve():
    for i in range(1, 1010): fc[i] = fc[i - 1] * i
    for i in range(1010): ifc[i] = inv(fc[i])
    num = 1
    dp = [[[0] * 1010 for _ in range(2)] for k in range(1010)]
    dpc = [0] * 1010
    f = [False] * 1010
    n = II()
    s = S()
    if n == 1 and s == "-":
        print("{} 0 {}".format((mod + 1) // 2, (mod + 1) // 2))
        return
    q = 0
    r = n
    n = -1
    if s[q] == "-":
        q += 1
    if s[q] == "-":
        q += 1
        n += 1
        num += 1
    if s[q] == "-":
        print("0 0 0")
        return
    for i in range(q, r):
        if s[i] == "X":
            if num == 0:
                print("0 0 0")
                return
            if n >= 0:
                f[n] = num - 1
            n += 1
            num = 0
        else:
            if num > 1:
                print("0 0 0")
                return
            num += 1
    if num == 2:
        f[n] = 1
        n += 1
    dpc[0] = 1
    for i in range(n):
        if f[i]:
            for j in range(2):
                for k in range(2 * n + 2):
                    kari = inv(k * k + 3 * k + 2)
                    dp[i + 1][j][0] = ad(dp[i + 1][j][0], mlt(dp[i][j][k], kari))
                    dp[i + 1][j][1] = ad(dp[i + 1][j][1], mlt(dp[i][j][k], mod - kari))
            dp[i + 1][1][0] = ad(dp[i + 1][1][0], dpc[i])
            dp[i + 1][1][1] = ad(dp[i + 1][1][1], mod - dpc[i])
        else:
            for j in range(2):
                for k in range(2 * n + 2):
                    kari = inv(k + 1)
                    dp[i + 1][j][0] = ad(dp[i + 1][j][0], mlt(dp[i][j][k], kari))
                    dp[i + 1][j][1] = ad(dp[i + 1][j][1], mlt(dp[i][j][k], mod - kari))
                    dp[i + 1][j][k + 2] = ad(dp[i + 1][j][k + 2], mlt(dp[i][j][k], inv(k * k + 3 * k + 2)))
            dp[i + 1][1][1] = ad(dp[i + 1][1][1], dpc[i])
            dp[i + 1][1][0] = ad(dp[i + 1][1][0], mod - dpc[i])
            dpc[i + 1] = ad(dpc[i + 1], dpc[i])
    ans = [0] * 3
    for j in range(2):
        for k in range(2 * n + 2):
            ans[j] = ad(ans[j], mlt(dp[n][j][k], fc[k]))
            ans[j + 1] = ad(ans[j + 1], mlt(dp[n][j][k], mod - ad(fc[k], bn(k))))
    kari = (mod + 1) // 2
    ans[0] = ad(ans[0], mlt(dpc[n], kari))
    ans[2] = ad(ans[2], mlt(dpc[n], mod - kari))
    print("{} {} {}".format(ans[0], ans[1], ans[2]))
    return


#main
if __name__ == '__main__':
    solve()
