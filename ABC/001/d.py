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
def solve():
    n = II()
    se = [list(map(int, input().split("-"))) for _ in range(n)]
    for i in range(n):
        se[i][0] = (se[i][0] // 5) * 5
        se[i][1] = math.ceil(se[i][1] / 5) * 5
        if (se[i][1] - 60) % 100 == 0:
            se[i][1] = se[i][1] + 40
    se.sort()
    ans = [[se[0][0], se[0][1]]]
    x = 0
    for i, k in se:
        if ans[x][1] >= i:
            ans[x][1] = max(k,ans[x][1])
        else:
            ans.append([i, k])
            ans[x][0] = "000" + str(ans[x][0])
            ans[x][1] = "000" + str(ans[x][1])
            ans[x][0] = ans[x][0][-4:]
            ans[x][1] = ans[x][1][-4:]
            print('{}-{}'.format(ans[x][0],ans[x][1]))
            x += 1
    ans[x][0] = "000" + str(ans[x][0])
    ans[x][1] = "000" + str(ans[x][1])
    ans[x][0] = ans[x][0][-4:]
    ans[x][1] = ans[x][1][-4:]
    print('{}-{}'.format(ans[x][0],ans[x][1]))
    return


#main
if __name__ == '__main__':
    solve()
