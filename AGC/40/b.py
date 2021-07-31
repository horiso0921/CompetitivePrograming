
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
def B():
    n = II()
    LR = LIR(n)
    LR.sort(key=lambda x: (x[1] - x[0], -x[1]))
    ans = [[LR[0][0], LR[0][1] + 1], [LR[1][0], LR[1][1] + 1]]
    for i in range(2, n):
        l, r = LR[i]
        r += 1
        a12 = min(ans[0][1], ans[1][1]) - max(ans[0][0], ans[1][0])
        a12 = (a12 > 0) * a12 + r - l
        a12 = (a12 > 0) * a12
        a1lr = min(ans[0][1], r) - max(ans[0][0], l)
        a1lr = (a1lr > 0) * a1lr + ans[1][1] - ans[1][0]
        a1lr = (a1lr > 0) * a1lr
        a2lr = min(ans[1][1], r) - max(ans[1][0], l)
        a2lr = (a2lr > 0) * a2lr + ans[0][1] - ans[0][0]
        a2lr = (a2lr > 0) * a2lr
        res = [(a12, 0), (a1lr, 1), (a2lr, 2)]
        res.sort(reverse=True)
        if res[0][1] == 0:
            ans[0] = [max(ans[0][0], ans[1][0]), min(ans[0][1], ans[1][1])]
            ans[1] = [l, r]
        elif res[0][1] == 1:
            ans[0] = [max(ans[0][0], l), min(ans[0][1], r)]
        else:
            ans[1] = [max(ans[1][0], l), min(ans[1][1], r)]
    a = ans[0][1] - ans[0][0]
    b = ans[1][1] - ans[1][0]
    print((a > 0) * a + (b > 0) * b)

    return

