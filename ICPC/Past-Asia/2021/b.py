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
    n = II()
    s = IR(n)
    twos = [0] * 100
    fours = [[0] * 100 for _ in range(100)]
    for si in s:
        two = si % 100
        four = (si % 10000) // 100
        twos[two] += 1
        fours[two][four] += 1
    fours_l = [sorted([(-fours[i][j], j) for j in range(100)]) for i in range(100)]
    twos_l = sorted([(-twos[i], i) for i in range(100)])
    
    ans = 0
    for t in range(100):
        sc4,f = fours_l[t][0]
        aa = 0
        tmp = sc4 * 4000
        for sc2, two in twos_l:
            if t == two: continue
            if aa == 3: break
            aa += 1
            tmp += sc2 * 500
        ans = min(tmp, ans)

    for si in s:
        four = si % 10000
        two = si % 100
        for t in range(100):
            tmp = -300000
            sc4,f = fours_l[t][0]
            if t == two:
                sc4,f = 0, 0
            aa = 0
            tmp += sc4 * 4000
            for sc2, two_ in twos_l:
                if t == two_: continue
                if two == two_: continue
                if aa == 3: break
                aa += 1
                tmp += sc2 * 500
            if ans > tmp:
                ans = tmp
                
    print(-ans)
            
        

    return


#main
if __name__ == '__main__':
    solve()