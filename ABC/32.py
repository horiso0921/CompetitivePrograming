#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    a, b, n = II(), II(), II()
    while 1:
        if not (n % a or n % b):
            print(n)
            break
        n += 1
    return

#B
def B():
    s = S()
    k = II()
    d = defaultdict(int)
    ls = len(s)
    for i in range(ls - k + 1):
        d[tuple(s[i:i + k])] += 1
    print(len(d.keys()))

    return

#C
def C():

    n, k = LI()
    s = IR(n)

    if 0 in s:
        print(n)
        return

    l = 0
    r = 0
    now = 1
    ans = 0
    if k == 0:
        print(0)
        return

    while r < n:
        if now <= k:
            ans = max(ans, r - l)
            now *= s[r]
            r += 1
        else:
            now /= s[l]
            l += 1

    if now <= k:
        ans = max(ans, r - l)
    print(ans)
    return

# D
# 解説AC
# n <= 30以外の場合はDP
# だだし、dp[i][j]といったような二重リストだと
# pythonでは厳しい
# dp[i]として
# 価値iにおける最低の荷量
# 荷量iにおける最大の価値
# の2通りでできる
# n <= 30の倍が鬼門
# 2 ** nの全探索（どれを使うか）ではダメ
# 半分ずつに分けて二分探索で解を求めるという変態手法
# なんだこれ！？！？ 

def D():
    n, W = LI()
    vw = []
    maxw = 0
    maxv = 0
    for _ in range(n):
        v, w = LI()
        maxw = max(maxw, w)
        maxv = max(maxv, v)
        vw.append((v, w))

    if n <= 30:
        n1 = n // 2
        n2 = n - n1
        vw1 = vw[:n1]
        vw2 = vw[n1:]
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        lis1 = []
        lis2 = []
        fullserch1 = itertools.product(range(2), repeat=n1)
        fullserch2 = itertools.product(range(2), repeat=n2)
        ans = 0

        for fulls in fullserch1:
            v, w = [0] * 2
            for i, full in enumerate(fulls):
                if full:
                    v += vw1[i][0]
                    w += vw1[i][1]
            d1[w] = max(d1[w], v)
        pre = -1
        l = list(d1.items())
        l.sort(key=lambda x: x[0])
        for key, value in l:
            if value > pre:
                lis1.append(key)
                pre = value

        for fulls in fullserch2:
            v, w = [0] * 2
            for i, full in enumerate(fulls):
                if full:
                    v += vw2[i][0]
                    w += vw2[i][1]
            d2[w] = max(d2[w], v)
        pre = -1
        l = list(d2.items())
        l.sort(key=lambda x: x[0])
        for key, value in l:
            if value > pre:
                lis2.append(key)
                pre = value

        for l1 in lis1:
            x = bisect_right(lis2, W - l1) - 1
            if x == -1:
                continue
            ans = max(ans, d1[l1]+d2[lis2[x]])

        print(ans)
        return

    if 1 <= maxw <= 1000:
        dp = [-inf] * (maxw * n + 1)
        dp[0] = 0
        vw.sort(key=lambda x: x[1])
        for v, w in vw:
            for j in range(maxw * n, w - 1, -1):
                dp[j] = max(dp[j], dp[j - w] + v)
        print(max(dp[:W+1]))
        return

    if 1 <= maxv <= 1000:
        dp = [inf] * (maxv * n + 1)
        dp[0] = 0
        for v,w in vw:
            for j in range(maxv * n, v - 1, -1):
                dp[j] = min(dp[j], dp[j - v] + w)
        ans = 0
        for i in range(maxv * n + 1):
            if dp[i] <= W:
                ans = max(ans, i)
        print(ans)
    return

#Solve
if __name__ == '__main__':
    D()
