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
    a1, a2, a3 = LI()
    ans = 0
    for full in itertools.permutations(range(a1 + a2 + a3), a1 + a2 + a3):
        f = list(full)
        ff = 0
        for i in range(a1 + a2 + a3):
            if i < a1:
                if i + 1 < a1:
                    if f[i] < f[i + 1]:
                        pass
                    else:
                        ff = True
                if i + a1 < a1 + a2:
                    if f[i] < f[i + a1]:
                        pass
                    else:
                        
                        ff = True
            elif i < a1 + a2:
                if i + 1 < a1 + a2:
                    if f[i] < f[i + 1]:
                        pass
                    else:
                        
                        ff = True
                if i + a2 < a1 + a2 + a3:
                    if f[i] < f[i + a2]:
                        pass
                    else:
                        
                        ff = True
            else:
                if i + 1 < a1 + a2 + a3:
                    if f[i] < f[i + 1]:
                        pass
                    else:
                        
                        ff = True

        if ff:
            continue
        ans += 1
    print(ans)


    return


#main
if __name__ == '__main__':
    solve()
