
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
# k <= nなら制約からシミュレーションすればいいことがわかる
# k > nのとき閉路が発生してかつ閉路の中で状態が終了する
# 1 → 2 → 3 → 4 → 5 → 6
#         ↑           ↓
#         ↑ ← 9 ← 8 ← 7
# 閉路サイズ7 スタート1
# k=10とするなら10%7=3
# 閉路に入るまでの距離が2なので
# 1からシミュレーションする
# k=15とするなら15%7=1
# 閉路に入るまでの距離より小さいので
