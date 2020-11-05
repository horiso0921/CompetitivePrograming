#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
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
def IR(n):
    res = [None] * n
    for i in range(n):
        res[i] = II()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI()
    return res
def FR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIF(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def SR(n):
    res = [None] * n
    for i in range(n):
        res[i] = S()
    return res
def LSR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LS()
    return res
mod = 1000000007
inf = float('INF')

#solve
def solve():
    n = II()
    a = LI()
    b = LI()
    ans = [None] * n
    odd = []
    even = []
    check = [False] * n
    for i in range(n):
        t = - a[i] + b[i]
        ans[i] = (t, i)
        if i & 1:
            heappush(odd, (-t, i))
        else:
            heappush(even, (-t, i))
            
    cnt = sum(a)
    ans.sort(reverse=1)
    for s, i in ans:
        if check[i]: continue
        if i & 1:
            while even:
                t, ti = heappop(even)
                if check[ti]: continue
                t *= - 1
                if s + t > 0:
                    cnt += s + t
                    check[i] = 1
                    check[ti] = 1
                break
        else:
            while odd:
                t, ti = heappop(odd)
                if check[ti]: continue
                t *= - 1
                if s + t > 0:
                    cnt += s + t
                    check[i] = 1
                    check[ti] = 1
                break
    print(cnt)
    return


#main
if __name__ == '__main__':
    solve()
