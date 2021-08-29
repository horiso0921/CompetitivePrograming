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
def solve():
    n = II()
    e = LIR(n)
    ans = [[0] * n for i in range(n)]
    ttans = 0
    for xi in range(2, 100):
        elis = []
        for i in range(n):
            for j in range(n):
                heappush(elis,(-e[i][j], i, j))
        ans_tmp = 0
        tans = [[0] * n for i in range(n)]
        check = [[0] * n for i in range(n)]
        def cf(i,j,r,ee):
            i += r
            tmp = []
            for x in range(r):
                tmp.append((i,j))
                i -= 1
                j -= 1
            for x in range(r):
                tmp.append((i,j))
                i -= 1
                j += 1
            for x in range(r):
                tmp.append((i,j))
                i += 1
                j += 1
            for x in range(r):
                tmp.append((i,j))
                i += 1
                j -= 1
            tt = ee * xi
            for i,j in tmp:
                if 0 <= i < n and 0 <= j < n:
                    if tans[i][j]: return 0
                    for mi,mj in [(0,1),(1,0),(-1,0),(0,-1)]:
                        mi += i
                        mj += j
                        if 0 <= mi < n and 0 <= mj < n and check[mi][mj] == 0:
                            tt -= e[mi][mj]
            
            if tt < 0: return 0
            for i,j in tmp:
                if 0 <= i < n and 0 <= j < n:
                    check[i][j] = 1
            return True
        while elis:
            _, i, j = heappop(elis)
            if check[i][j]: continue
            check[i][j] = 1
            for x in range(1, n+1):
                xx = cf(i,j,x,e[i][j])
                if xx: continue
                break
            else:
                tans[i][j] = n
                ans_tmp += n * e[i][j]
                continue
            tans[i][j] = x - 1
            ans_tmp += (x - 1) * e[i][j]
        if ttans < ans_tmp:
            ans = tans
            ttans = ans_tmp
    for ai in ans:
        print(*ai)
    return


#main
if __name__ == '__main__':
    solve()