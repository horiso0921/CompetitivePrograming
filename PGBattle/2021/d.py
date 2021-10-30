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
def S(): return input().rstrip()
def LS(): return S().split()
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
【PGBATTLE2021:かつおぶし】コイン投げ
配点 : 30点問題難易度 : 目安解答時間 : 30分
制限実行時間 : 2秒制限メモリ使用量 : 1048MB
問題文
H と T からなる文字列 
S
 、および表と裏が等確率で出るコインが与えられます。

あなたはこのコインを投げ続け、その最後 
|
S
|
 回の結果が 
S
 に一致したらコインを投げるのを終了します。( H は表を、 T は裏を意味します。)

厳密に言い換えると、はじめに 
|
S
|
 個の U からなる文字列 
U
 があります。あなたは 
U
 が 
S
 と一致するまで次の操作を行います。

コインを投げて表が出たら 
U
 の末尾に H を、裏が出たら T を追加する。その後、 
U
 の先頭の要素を削除する。
コインを投げる回数の期待値を 
998244353
 で割ったあまりを求めてください。答えは整数であることが証明できます。"""

#solve
def solve():
    return


#main
if __name__ == '__main__':
    solve()