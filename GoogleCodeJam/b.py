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
def solve(n):
    ans = []
    bit = 0
    tmpn = n
    while n:
        n >>= 1
        bit += 1
    f = 0
    for i in range(bit - 1, -1, -1):
        tmp = (1 << i) + i
        if tmp > tmpn:
            tmpn -= f
            continue
        tmpn -= 1 << i
        f = 1
        ans.append(i + 1)
    ans = ans[::-1]
    res = []
    i = 1
    j = 1
    for ai in ans:
        for i in range(i, ai):
            if j == 1:
                res.append((i, j))
            else:
                j += 1
                res.append((i, j))
        i = ai + 1
        if j != 1:
            for j in range(j + 1, 0, -1):
                res.append((ai, j))
        else:
            for j in range(1, ai + 1):
                res.append((ai, j))
    for i in range(tmpn):
        ai += 1
        j += j != 1
        res.append((ai, j))
    return res


#main
if __name__ == '__main__':
    ans = []
    for _ in range(II()):
        ans.append(solve(II()))
    for i, ai in enumerate(ans):
        print("Case #{}:".format(i + 1))
        for a in ai:
            print(*a)
