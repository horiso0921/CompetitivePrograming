
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
# 鈍角三角形には鈍角が一つだけ
# 直角三角形には直角が一つだけ
# あることがミソ
# 鈍角になる3点と直角になる3点の数を出せばよい
# 1点を決めてn点間の水平からの角度を出す((-1,0)が-180°)
# そのn点から時計回りに90°,90°~180°になる点の数は
# 尺取り法なり二分探索なりで求められるためそれで終わり
def D():
    n = II()
    xy = LIR(n)
    right = 0
    obtuse = 0
    for x, y in xy:
        lis = []
        for xi, yi in xy:
            if x == xi and y == yi:
                continue
            the = degrees(atan2(yi - y, xi - x))
            lis.append(the)
            lis.append(the + 360)
        lis.sort()
        llis = len(lis)
        for l in lis[:llis // 2]:
            right += bisect_right(lis, l + 90 + 1e-9) - bisect_left(lis, l + 90 - 1e-9)
            obtuse += bisect_right(lis, l + 180 + 1e-9) - bisect_right(lis, l + 90 + 1e-9)
    print(n * (n - 1) * (n - 2) // 6 - right - obtuse, right, obtuse)
    return

