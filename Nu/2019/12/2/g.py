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
def LS(): return input().split()
def S(): return list(input().rstrip())
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
    k, n = LI()
    vw = LSR(n)
    fulls = itertools.product(range(1, 4), repeat=k)
    for full in fulls:
        d = defaultdict(str)
        full = list(full)
        for v, w in vw:
            res = 0
            for vi in v:
                if d[vi]:
                    pass
                else:

                    d[vi] = w[res: res + full[int(vi) - 1]]
                res += full[int(vi) - 1]
                if res >= len(w):
                    break
            tmp = ""
            for vi in v:
                tmp = tmp + d[vi]
            if tmp == w:
                continue
            else:
                break
        else:
            ans = d.items()
            ans = sorted(ans)
            for _, value in ans:
                print (value)
            return
    return


#main
if __name__ == '__main__':
    solve()
