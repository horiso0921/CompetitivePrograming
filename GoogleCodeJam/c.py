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
    r, c = LI()
    s = LIR(r)
    res = 0
    tmp = 1
    while tmp != 0:
        tmp = 0
        x = []
        for i in range(r):
            for j in range(c):
                res += s[i][j]
                if s[i][j] == 0:
                    continue
                tmp1 = 0
                tmp2 = 0
                for u in range(i - 1, -1, -1):
                    if s[u][j]:
                        tmp1 += s[u][j]
                        tmp2 += 1
                        break
                for d in range(i + 1, r):
                    if s[d][j]:
                        tmp1 += s[d][j]
                        tmp2 += 1
                        break
                for l in range(j - 1, -1, -1):
                    if s[i][l]:
                        tmp1 += s[i][l]
                        tmp2 += 1
                        break
                for rr in range(j + 1, c):
                    if s[i][rr]:
                        tmp1 += s[i][rr]
                        tmp2 += 1
                        break
                if tmp1 > s[i][j] * tmp2:
                    x.append((i, j))
                    tmp = 1
        for i, j in x:
            s[i][j] = 0
    return res


#main
if __name__ == '__main__':
    ans = []
    for _ in range(II()):
        ans.append(solve())
    for i, ai in enumerate(ans):
        print("Case #{}: {}".format(i+1, ai))
