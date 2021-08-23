
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
# なんていうか脳みそが足りない
# 制限速度に落とし込むのはわかったけど。。。
# 一つの制限速度にに対して
# 0<=x<=l なら v+(l-x) 
# l<=x<=r なら v 
# r<=x<=T なら v+(x-r)
# つらい
def D():
    n = II()
    t = LI()
    v = LI()
    t += [0]
    v = [0] + v + [0]
    time = [[0, 0]]
    for i in range(1, n+2):
        time.append((time[-1][1], time[-1][1] + t[i - 1]))
    def vx(x):
        res = inf
        for i in range(n+2):
            res = min(res, f(i, x))
        return res
    def f(i, x):
        l, r = time[i]
        vi = v[i]
        return vi + (l - x) if 0 <= x <= l else vi if l <= x <= r else vi + (x - r)
    ans = 0
    for x in range(sum(t) * 2):
        ans += 0.25 * (vx(x/2) + vx(x/2 + 0.5))
    print(ans)
    return

