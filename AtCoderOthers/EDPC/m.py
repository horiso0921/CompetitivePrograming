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
inf = 1e10

"""
URL: https://atcoder.jp/contests/dp/tasks/dp_m

M - Candies / 
実行時間制限: 2 sec / メモリ制限: 1024 MB

配点 : 100 点

問題文
N 人の子供たちがいます。 子供たちには 1,2,…,N と番号が振られています。
子供たちは K 個の飴を分け合うことにしました。 
このとき、各 i (1≤i≤N) について、子供 i が受け取る飴の個数は \
    0 以上 ai 以下でなければなりません。 
また、飴が余ってはいけません。

子供たちが飴を分け合う方法は何通りでしょうか？ 109+7 で割った余りを求めてください。 
ただし、2 通りの方法が異なるとは、ある子供が存在し、その子供が受け取る飴の個数が異なることを言います。


解法
dp[i][k] (i人目にk個使用した時)で回すだけ
累積和でO()削減
"""

#solve
def solve():
    n, k = LI()
    a = LI()
    dp = [0] * (k + 1)
    acc = [1] * (k + 1)
    dp[0] = 1
    for i in range(n):
        for l in range(1, k + 1):
            dp[l] = acc[l]
            dp[l] -= acc[l - a[i] - 1] if l - a[i] > 0 else 0
            dp[l] %= mod
        for l in range(1, k + 1):
            acc[l] = acc[l - 1] + dp[l]
            acc[l] %= mod
    print(dp[-1])


    return


#main
if __name__ == '__main__':
    solve()
