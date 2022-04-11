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
inf = float("INF")

#solve
def solve():
    n,m = LI()
    abc = LIR_(m)
    edg = [[] for _ in range(n)]
    dist = [[inf] * n for _ in range(n)]
    ee = defaultdict(int)
    ans = defaultdict(int)
    for a,b,c in abc:
        dist[a][b] = c + 1
        dist[b][a] = c + 1
    for i in range(n):
        dist[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
    ans = 0
    for a,b,c in abc:
        c += 1
        d = dist[a][b]
        for m in range(n):
            if m != a and m != b:
                if dist[a][m] + dist[m][b] == d:
                    ans += 1
                    break
    print(ans)
                
    return


#main
if __name__ == '__main__':
    solve()