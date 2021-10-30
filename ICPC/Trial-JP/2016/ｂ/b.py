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
def solve(s):
    s_field = s.split("/")
    field = []
    for si in s_field:
        f = []
        for i in si:
            if i == "b":
                f.append("b")
            else:
                for _ in range(int(i)):
                    f.append(".")
        field.append(f)
    a,b,c,d = LI_()
    field[c][d] = "b"
    field[a][b] = "."
    ans = []
    for si in field:
        tt = []
        tmp = 0
        for j in si:
            if j == "b":
                if tmp:
                    tt.append(str(tmp))
                tt.append("b")
                tmp = 0
            else:
                tmp += 1
        if tmp:
            tt.append(str(tmp))
        ans.append("".join(tt))
    print("/".join(ans))
    return


#main
if __name__ == '__main__':
    while 1:
        s = S()
        if s == "#": break
        solve(s)