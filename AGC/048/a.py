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
    t = II()
    check = "atcoder"
    for _ in range(t):
        ans = inf
        tmp = 0
        s = S()
        if s > check:
            print(0)
            continue
        pre = []
        cc = set()
        for ci in range(7):
            c = check[ci]
            t = 0
            tmp1 = inf
            tmp2 = inf
            for i in range(len(s)):
                if not (t & 1) and s[i] > c:
                    tmp1 = i
                    t |= 1 
                if not (t & 2) and s[i] == c and i not in cc:
                    tmp2 = i
                    cc.add(i)
                    t |= 2
                if t >= 3:
                    break
            if t == 0:
                if ans == inf:
                    print(-1)
                else:
                    print(ans)
                break
            for p in pre:
                if p > tmp1:
                    tmp1 += 1
                if p > tmp2:
                    tmp2 += 1
            tmp1 = abs(ci - tmp1)
            ans = min(ans, tmp + tmp1)
            tmp += abs(ci - tmp2)
            pre.append(tmp2)
        else:
            print(ans)
    return


#main
if __name__ == '__main__':
    solve()
