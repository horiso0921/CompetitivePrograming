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
    for i in range(II()):
        cmyk = LIR(3)
        min_cmyk = [inf, inf, inf, inf]
        for j in range(4):
            min_cmyk[j] = min((x[j] for x in cmyk))
        # print(min_cmyk)
        print(f"Case #{i+1}:", end="")
        if sum(min_cmyk) < 10 ** 6:
            print(" IMPOSSIBLE")
        else:
            tmp = 10 ** 6
            for i in range(4):
                if tmp > min_cmyk[i]:
                    print(f" {min_cmyk[i]}", end="")
                    tmp -= min_cmyk[i]
                else:
                    print(f" {tmp}", end="")
                    tmp = 0
            print()
        
    return


#main
if __name__ == '__main__':
    solve()