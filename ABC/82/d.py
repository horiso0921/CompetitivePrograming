
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
# X,Y軸に分解して、移動は常に同じ方向に行われる（TFFFTならFは常に同じ方向）
# ためTFFFFFTFFFF→TF5TF4として考えて奇数番目のFがx偶数番目がyに寄与
# あとはDP
s = S()
X, Y = LI()
dx = defaultdict(int)
dy = defaultdict(int)
i = 0
num = 0
lis = []
for i in range(len(s)):
    if s[i] == "T":
        lis.append(num)
        num = 0
    else:
        num += 1
if s[-1] == "F":
    lis.append(num)
dx[lis[0]] = True
dy[0] = True
for i in range(1, len(lis)):
    if not i % 2:
        ndx = defaultdict(int)
        for key, _ in dx.items():
            ndx[key + lis[i]] = True
            ndx[key - lis[i]] = True
        dx = ndx
    else:
        ndy = defaultdict(int)
        for key, _ in dy.items():
            ndy[key + lis[i]] = True
            ndy[key - lis[i]] = True
        dy = ndy
if dx[X] and dy[Y]:
    print("Yes")
else:
    print("No")