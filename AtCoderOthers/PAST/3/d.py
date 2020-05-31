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
inf = float('INF')

#solve
def solve():
    n = II()
    s1 = S()
    s2 = S()
    s3 = S()
    s4 = S()
    s5 = S()
    d = {}
    d["####.##.##.####"] = 0
    d[".#.##..#..#.###"] = 1
    d["###..#####..###"] = 2
    d["###..####..####"] = 3
    d["#.##.####..#..#"] = 4
    d["####..###..####"] = 5
    d["####..####.####"] = 6
    d["###..#..#..#..#"] = 7
    d["####.#####.####"] = 8
    d["####.####..####"] = 9
    for i in range(1, n + 1):
        tmp = s1[4*i-3:4*i]+s2[4*i-3:4*i]+s3[4*i-3:4*i]+s4[4*i-3:4*i]+s5[4*i-3:4*i]
        print(d[tmp], end="")
    return


#main
if __name__ == '__main__':
    solve()
