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
    tmp = [(1,1)]
    for i in range(2, 10 ** 4):
        tmp.append((tmp[-1][0] + i, i))

    ans = []
    ttt = []
    for t,i in tmp[::-1]:
        while t <= n:
            for _ in range(i):
                ans.append("7")
            tt = [1] * 7
            nt = 0
            for ti in ttt[::-1]:
                nt += int(ans[ti]) * pow(10, len(ans) - ti, 7)
                nt %= 7
                tt[-nt % 7] = 0
            ttt.append(len(ans))
            for kk in range(1, 7):
                if tt[kk]:
                    ans.append(str(kk))
                    break
            else:
                raise RuntimeError
            n -= t
    print("".join(ans))
        
    return


#main
if __name__ == '__main__':
    solve()