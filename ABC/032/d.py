
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

