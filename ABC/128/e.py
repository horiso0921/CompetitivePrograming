
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
def E():  
    N,q = LI()
    STX = LIR(N)
    D = IR(q)
    LV = (q - 1).bit_length()
    N0 = 1 << LV

    data = [inf] * (N0 << 1)
    INF = inf

    def update(l, r, x):
    
        #  区間[l, r)のdataの値を更新
        L = N0 + l; R = N0 + r
        while L < R:
            if R & 1:
                R -= 1
                data[R-1] = min(data[R-1], x)
            if L & 1:
                data[L-1] = min(data[L-1], x)
                L += 1
            L >>= 1; R >>= 1

    def query(x):
        L = N0 + x - 1
        #  xの最小値を求める
        s = INF
        while L >= 0:
            s = min(s, data[L])
            L = (L - 1) >> 1
        return s

    for s, t, x in STX:
        XS = max(-1, s - x)
        XT = max(-1, t - x)
        XS_index = bisect_left(D, XS)
        XT_index = bisect_left(D, XT)
        update(XS_index, XT_index, x)

    for i in range(q):
        a = query(i)
        print(a if a != inf else -1)
