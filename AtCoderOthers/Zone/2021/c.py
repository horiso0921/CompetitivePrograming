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
    l = list(itertools.product(range(3), repeat=5))
    n = II()
    abcde = LIR(n)
    ok = 0
    ng = 10 ** 9 + 1
    def f(m):
        for mask in l:
            x = []
            y = []
            z = []
            for i in range(5):
                if mask[i] == 0:
                    x.append(i)
                elif mask[i] == 1:
                    y.append(i)
                else:
                    z.append(i)
            for aa in abcde:
                if x:
                    for xi in x:
                        if aa[xi] < m:
                            break
                    else:
                        x = []
                if y:
                    for xi in y:
                        if aa[xi] < m:
                            break
                    else:
                        y = []
                if z:
                    for xi in z:
                        if aa[xi] < m:
                            break
                    else:
                        z = []
            if x or y or z:
                continue
            return True
        return False



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
    