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
def LS(): return input().split()
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
    def f(point, pre):
        p = lis[point]
        for nex in edg[point]:
            if nex == pre:
                continue
            lis[nex] = p + 1
            f(nex, point)
        return
    n = II()
    ab = LIR_(n - 1)
    lis = [-1] * n
    edg = [[] for _ in range(n)]
    for a, b in ab:
        edg[a].append(b)
        edg[b].append(a)
    lis[0] = 1
    f(0, -1)
    d = [0, 0]
    for i in lis:
        d[i & 1] += 1
    ans = [None] * n
    if d[0] <= n // 3:
        t = 1
        for i in range(n):
            if lis[i] & 1:
                continue
            ans[i] = str(t * 3)
            t += 1
        m = t * 3
        t = 1
        for i in range(n):
            if ans[i]:
                continue
            ans[i] = str(t)
            t += 1
            if t >= m:
                continue
            if t % 3 == 0:
                t += 1
    elif d[1] <= n // 3:
        t = 1
        for i in range(n):
            if not lis[i] & 1:
                continue
            ans[i] = str(t * 3)
            t += 1
        m = t * 3
        t = 1
        for i in range(n):
            if ans[i]:
                continue
            ans[i] = str(t)
            t += 1
            if t >= m:
                continue
            if t % 3 == 0:
                t += 1
    else:
        t = n // 3
        odd = 1
        even = 2
        for i in range(n):
            if t:
                if lis[i] & 1:
                    if d[1] <= n // 3 + (n % 3 >= 1):
                        ans[i] = str(odd)
                        odd += 3
                    else:
                        ans[i] = str(3 * t)
                        t -= 1
                        d[1] -= 1
                else:
                    if d[0] <= n // 3 + (n % 3 >= 2):
                        ans[i] = str(even)
                        even += 3
                    else:
                        ans[i] = str(3 * t)
                        t -= 1
                        d[0] -= 1 
            else:
                if lis[i] & 1:
                    ans[i] = str(odd)
                    odd += 3
                else:
                    ans[i] = str(even)
                    even += 3
    print(" ".join(ans))


    return


#main
if __name__ == '__main__':
    solve()
