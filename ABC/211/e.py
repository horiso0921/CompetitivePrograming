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
    k = II()
    s = SR(n)
    ans = 0
    for i in range(n):
        for j in range(n):
            if s[i][j] == "#": continue
            check = defaultdict(set)
            check[1<<(i*n+j)] = {i*n+j}
            nev = i * n + j
            for _ in range(k-1):
                ncheck = defaultdict(set)
                for key, val in check.items():
                    for vi in val:
                        if vi // n != 0:
                            vj = vi - n
                            vx,vy = divmod(vj, n)
                            if nev < vj and s[vx][vy] == ".": 
                                if not (key >> vj) & 1:
                                    ncheck[key | (1 << vj)].add(vj)
                        if vi // n != n-1:
                            vj = vi + n
                            vx,vy = divmod(vj, n)
                            if nev < vj and s[vx][vy] == ".":
                                if not (key >> vj) & 1:
                                    ncheck[key | (1 << vj)].add(vj)
                        if vi % n != 0:
                            vj = vi - 1
                            vx,vy = divmod(vj, n)
                            if nev < vj and s[vx][vy] == ".":
                                if not (key >> vj) & 1:
                                    ncheck[key | (1 << vj)].add(vj)
                        if vi % n != n-1:
                            vj = vi + 1
                            vx,vy = divmod(vj, n)
                            if nev < vj and s[vx][vy] == ".":
                                if not (key >> vj) & 1:
                                    ncheck[key | (1 << vj)].add(vj)
                print(check)
                check = ncheck
            ans += len(check.keys())
            print(ans)

    return


#main
if __name__ == '__main__':
    solve()