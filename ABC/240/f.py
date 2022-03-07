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
    t = II()
    for _ in range(t):
        n,m = LI()
        xy = LIR(n)
        ok = -4 * m
        ng = (1 + m) * m // 2 * 4 + 1
        def f(mid):
            tmp = 0
            jumprange = 0
            for x,y in xy:
                # print(tmp)
                if tmp >= mid:
                    return True
                if x >= 0:
                    tmp += jumprange * y
                    tmp += (1 + y) * y // 2 * x
                    jumprange += x * y
                else:
                    # print(jumprange, 1)
                    if jumprange <= 0:
                        tmp += jumprange * y
                        tmp += (1 + y) * y // 2 * x
                        jumprange += x * y
                    else:
                        # if 1/2 + 2 * jumprange / x > 0:
                        if jumprange + x <= 0:
                            tmp += jumprange * y
                            tmp += (1 + y) * y // 2 * x
                            jumprange += x * y
                        else:
                            giriJump = math.ceil((-x - sqrt(x**2 - x * 4 * jumprange)) / 2 / x)
                            if giriJump >= y:
                                tmp += jumprange * y
                                tmp += (1 + y) * y // 2 * x
                                jumprange += x * y
                            else:
                                tmp += jumprange * giriJump
                                tmp += (1 + giriJump) * giriJump // 2 * x
                                if tmp >= mid:
                                    return True
                                else:
                                    y -= giriJump
                                    tmp += jumprange * y
                                    tmp += (1 + y) * y // 2 * x
                                    jumprange += x * y

            if tmp >= mid:
                return True
                                
                        
                
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if f(mid):
                ok = mid
            else:
                ng = mid
        print(ok)
    return


#main
if __name__ == '__main__':
    solve()