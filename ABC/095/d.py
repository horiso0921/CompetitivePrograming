
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
def D():
    n, c = LI()
    clock_wise = [0] * n
    clock_wise_max = [0] * n
    clock_wise_rev = [0] * n
    clock_wise_rev_max = [0] * n
    xv = LIR(n)
    clock_wise[0] = xv[0][1] - xv[0][0]
    clock_wise_rev[-1] = - c + xv[-1][1] + xv[-1][0]
    for i in range(1, n):
        clock_wise[i] = clock_wise[i - 1] + xv[i][1] - xv[i][0] + xv[i - 1][0]
        clock_wise_rev[-i - 1] = clock_wise_rev[-i] + xv[-i - 1][1] + xv[-i - 1][0] - xv[-i][0]
    clock_wise_max[0] = clock_wise[0]
    clock_wise_rev_max[-1] = clock_wise_rev[-1]
    for i in range(1,n):
        clock_wise_max[i] = max(clock_wise[i], clock_wise_max[i - 1])
        clock_wise_rev_max[-i - 1] = max(clock_wise_rev[-i - 1], clock_wise_rev_max[-i])
    ans = max(0, max(clock_wise), max(clock_wise_rev))
    for i in range(n - 1):
        ans = max(ans, clock_wise[i] + clock_wise_rev_max[i + 1] - xv[i][0])
        ans = max(ans, clock_wise_rev[-i - 1] + clock_wise_max[-i - 2] - (c - xv[-i - 1][0]))
    print(ans)
    return

