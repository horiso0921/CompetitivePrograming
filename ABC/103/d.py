
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
# 貪欲かよ
# 言われればその通りでbi昇順でソートしていれば
# 直前で取り除いたものに関してはその橋より左側
# の街について絶対に橋が途切れているからね
# fuck!!! 
def D():
    n, m = LI()
    d = defaultdict(int)
    for _ in range(m):
        a, b = LI_()
        d[a] = max(d[a], n-b)
    mi = 0
    ans = 0
    for i in range(n - 1):
        if mi < d[i]:
            mi = d[i]
        if i == n - mi - 1:
            mi = 0
            ans += 1
    print(ans)
    return

