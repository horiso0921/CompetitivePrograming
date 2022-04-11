#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from random import random
import sys, itertools, math
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
# import random
from functools import lru_cache

#solve
def solve():
    n = II()
    # a = [random.randint(1, 1000) for _ in range(n)]
    A = LI()

    MIN = 0
    MAX = 1
    @lru_cache(maxsize=None)
    def dfs(l, r):
        if l == r:
            return [(A[l], A[l])]
        res = []
        for m in range(l, r):
            dl = dfs(l, m)
            dr = dfs(m+1 , r)
            for ll, lr in dl:
                for rl, rr in dr:
                    if lr - rl > 0 != rr - ll > 0:
                        mi = min(abs(lr - rl), abs(rr - ll))
                    else:
                        mi = 0
                    ma = max(lr - rl, rr - ll)
                    res.append((mi, ma))
                    print(res,dl,dr)
                    print(lr - rl > 0, rr - ll > 0)
        a = [0] * 1002
        for l, r in res:
            a[l] += 1
            a[r+1] -= 1
        a = list(itertools.accumulate(a))
        pre = [None, None]
        res = []
        for i in range(1002):
            if a[i]:
                if pre[0] == None:
                    pre[0] = i
            else:
                if pre[0] != None:
                    pre[1] = i - 1
                    res.append(pre)
                    pre = [None, None]
        # print(l, r, mi, ma)
        return res
    print(dfs(0, n-1)[0])
    return


#main
if __name__ == '__main__':
    solve()