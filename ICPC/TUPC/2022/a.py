#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math, re
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
    n = II()
    s = S()
    lis = ["U", "T", "P", "C"]
    ans = 4
    for i in range(n-3):
        tmp = list(s[i:i+4])
        xx = 0
        for j in range(4):
            if tmp[j] == lis[j]:
                continue
            else:
                if lis[j] in tmp:
                    k = tmp.index(lis[j])
                    tmp[k], tmp[j] = tmp[j], tmp[k]
                xx += 1
        ans = min(ans, xx)
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()