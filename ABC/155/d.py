#!/usr/bin/env python3
import math
import itertools
import random
import sys
from collections import defaultdict, deque
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
inf = 1e10

#solve
def solve():
    def f(x):
        res = 0
        l = 0
        r = n - 1
        for ai in a:
            if ai == 0:
                res += 0 if x < 0 else n - 1
                print(res)
            else:
                if ai <= -1:
                    res -= ai * ai <= x
                    while l < n and a[l] * ai > x :
                        l += 1
                    res += n - l
                    print(l,res)
                else:
                    res -= ai * ai <= x
                    while a[r] * ai > x and r >= 0:
                        r -= 1
                    res += r + 1
                    print(r, res)
        print(res,x,"=====")
        return k <= res // 2
    n, k = LI()
    a = LI()
    a.sort()
    ok = 10 ** 18
    ng = -10 ** 18 - 1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        print(ok,ng,mid)
        if f(mid):
            ok = mid
        else:
            ng = mid
    # print(list(map(lambda x: 374999999999999999 / x if x != 0 else 0, a)))
    print(ok)
    return


#main
if __name__ == '__main__':
    solve()


#!/usr/bin/env python3
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
inf = 1e10

#solve


def solve():

    def f(x):
        res = 0
        for ai in a:
            if ai == 0:
                res += 0 if x < 0 else n - 1
            else:
                if ai <= -1:
                    res -= ai * ai <= x
                    ok = n
                    ng = -1
                    while ok - ng > 1:
                        mid = (ok + ng) // 2
                        if a[mid] * ai <= x:
                            ok = mid
                        else:
                            ng = mid
                    res += n - ok
                else:
                    res -= ai * ai <= x
                    ok = -1
                    ng = n
                    while abs(ok - ng) > 1:
                        mid = (ok + ng) // 2
                        if a[mid] * ai <= x:
                            ok = mid
                        else:
                            ng = mid
                    res += ok + 1
        return k <= res // 2
    n, k = LI()
    a = LI()
    a.sort()
    ok = 10 ** 18
    ng = -10 ** 18 - 1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
    return


#main
if __name__ == '__main__':
    solve()
