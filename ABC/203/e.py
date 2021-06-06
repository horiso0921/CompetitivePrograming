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

#solve
def solve():
    n,m = LI()
    xy = defaultdict(list)
    for _ in range(m):
        x,y = LI()
        xy[x].append(y)
    ans = defaultdict(int)
    ans[n] = 1
    for i, lis in sorted(xy.items()):
        tmp = defaultdict(int)
        for li in lis:
            if not ans[li]:
                if ((0 < li <= 2*n) and ((ans[li - 1] and tmp[li - 1] == 0) or (tmp[li - 1] == -1)) \
                    or ((0 <= li < 2*n) and ((ans[li + 1] and tmp[li + 1] == 0) or (tmp[li + 1] == -1)))):
                    ans[li] = 1
                    tmp[li] = 1
            elif tmp[li] == 1:
                continue
            else:
                if ((0 < li <= 2*n) and ((ans[li - 1] and tmp[li - 1] == 0) or (tmp[li - 1] == -1)) \
                    or ((0 <= li < 2*n) and ((ans[li + 1] and tmp[li + 1] == 0) or (tmp[li + 1] == -1)))):
                    ans[li] = 1
                else:
                    ans[li] = 0
                    tmp[li] = -1
    print(sum(ans.values()))

    return


#main
if __name__ == '__main__':
    solve()