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
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR_(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI_()
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
    for _ in range(II()):
        s = S()
        ss = defaultdict(int)
        for si in s:
            ss[si] += 1
        ls = []
        for key, value in ss.items():
            ls.append((key, value))
        ls.sort()
        m = II()
        b = LI()
        l = []
        x = 0
        c = defaultdict(int)
        tmp = []
        for i in range(m):
            if b[i] == 0:
                c[i] = 1
                tmp.append(i)
                x += 1
        l.append(tmp)
        while x != m:
            ll = []
            for i in range(m):
                if not c[i]:
                    tmp = 0
                    for li in l:
                        for j in li:
                            tmp += abs(i - j)
                    if tmp == b[i]:
                        ll.append(i)
                        x += 1
                        c[i] = 1
            l.append(ll)
        ans = ["A"] * m
        cs = defaultdict(int)
        for li in l:
            while 1:
                a = ls.pop()
                if len(li) <= a[1]:
                    for i in li:
                        ans[i] = a[0]
                    break
        print("".join(ans))
    return


#main
if __name__ == '__main__':
    solve()
