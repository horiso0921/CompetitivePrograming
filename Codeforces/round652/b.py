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
    t = II()
    for i in range(t):
        n = II()
        s = S()
        f = 0
        ans = []
        if s[0] == "1":
            tmp = [1, 1]
        else:
            tmp = [0, 1]

        for si in s[1:]:
            if si == "1":
                if tmp[0] == 1:
                    tmp[1] += 1
                else:
                    ans.append(tmp)
                    tmp = [1, 1]
            else:
                if tmp[0] == 0:
                    tmp[1] += 1
                else:
                    ans.append(tmp)
                    tmp = [0, 1]
        
        ans.append(tmp)
        aa = []
        pre = ans[0]
        if pre[0] == 0:
            aa.append(str(pre[0]) * pre[1])
            a = 0
        else:
            if len(ans[1:]):
                pass
            else:
                print(s)
                continue
        tmp = 0
        for a, b in ans[1:]:
            if a == 1:
                pre = [a, b]
            else:
                pre = 0
                tmp = 1
        if tmp:
            aa.append("0")
        if a:
            aa.append(str(pre[0]) * pre[1])
        if aa:
            print("".join(aa))
        else:
            print(0)

    return


#main
if __name__ == '__main__':
    solve()
