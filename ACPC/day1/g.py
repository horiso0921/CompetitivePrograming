#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def IR(n):
    return [I() for _ in range(n)]
def LIR(n):
    return [LI() for _ in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    n = I()
    e = LIR(n)
    dp = [[float("inf")]*n for _ in range(n)]
    pre = [[0]*n for _ in range(n)]
    dp[0][0] = 0
    for i in range(n):
        t = i*n
        ei = e[i]
        dpi = dp[i]
        prei = pre[i]
        for j in range(n):
            dpij = dp[i][j]
            k = i+1
            if k < n:
                dpk = dp[k]
                ek = e[k]
                prek = pre[k]
                nd = dpij+ei[k]
                if nd < dpk[j]:
                    dpk[j] = nd
                    prek[j] = t
                nd = dpij+ek[j]
                if nd < dpi[k]:
                    dpi[k] = nd
                    prei[k] = t
                nd = dpij+ei[k]+ek[j]
                if nd < dpk[k]:
                    dpk[k] = nd
                    prek[k] = t
            if i != j:
                k = j+1
                if k < n:
                    dpk = dp[k]
                    ek = e[k]
                    prek = pre[k]
                    nd = dpij+ei[k]
                    if nd < dpk[j]:
                        dpk[j] = nd
                        prek[j] = t
                    nd = dpij+ek[j]
                    if nd < dpi[k]:
                        dpi[k] = nd
                        prei[k] = t
                    nd = dpij+ei[k]+ek[j]
                    if nd < dpk[k]:
                        dpk[k] = nd
                        prek[k] = t
            t += 1
    i = j = n-1
    forward = []
    backward = []
    while i != 0 or j != 0:
        t = pre[i][j]
        ni,nj = t//n,t%n
        if i != ni:
            forward.append(ni+1)
        if j != nj:
            backward.append(nj+1)
        i,j = ni,nj
    ans = forward[::-1] + [n] + backward
    print(dp[-1][-1])
    print(len(ans))
    print(*ans)
    return

#Solve
if __name__ == "__main__":
    solve()


