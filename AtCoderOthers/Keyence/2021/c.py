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
def LFR(n): return [LF() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 998244353
inf = 1e10

#solve
def solve():
    h,w,k = LI()
    field = [["Z"] * w for i in range(h) ]
    Zhi = [[0] * w for i in range(h) ]
    Zwi = [[0] * w for i in range(h) ]
    for _ in range(k):
        hi,wi,c = LS()
        hi=int(hi)-1
        wi=int(wi)-1
        field[hi][wi] = c
    for y in range(h):
        for x in range(w-1):
            Zwi[y][x+1] = Zwi[y][x] + (field[y][x] == "Z") 
    for x in range(w):
        for y in range(h-1):
            Zhi[y+1][x] = Zhi[y][x] + (field[y][x] == "Z") 
    pow3 = [3 for i in range(5001)]
    pow3[0] = 1
    for i in range(5000):
      pow3[i+1] *= pow3[i]
      pow3[i] %= mod
    return
    dp = [[0] * w for i in range(h)]
    dp[0][0] = 1
    for y in range(h):
        for x in range(w):
            if field[y][x] == "X":
                if x + 1 < w:
                    dp[y][x+1] += dp[y][x] * pow3[Zhi[y][x+1]]
                    dp[y][x+1] %= mod
                if y + 1 < h:
                    dp[y+1][x] += dp[y][x] * pow3[Zwi[y+1][x]]
                    dp[y+1][x] %= mod
            elif field[y][x] == "R":
                if x + 1 < w:
                    dp[y][x+1] += dp[y][x] * pow3[Zhi[y][x+1]]
                    dp[y][x+1] %= mod
            elif field[y][x] == "D":
                if y + 1 < h:
                    dp[y+1][x] += dp[y][x] * pow3[Zwi[y+1][x]]
                    dp[y+1][x] %= mod
            else:
                if x + 1 < w:
                    dp[y][x+1] += dp[y][x] * 2 * pow3[Zhi[y][x+1]]
                    dp[y][x+1] %= mod
                if y + 1 < h:
                    dp[y+1][x] += dp[y][x] * 2 * pow3[Zwi[y+1][x]]
                    dp[y+1][x] %= mod
    print(dp[-1][-1])
        
        
    return


#main
if __name__ == '__main__':
    solve()