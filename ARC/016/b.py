# !/usr/bin/env python3
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
def LS(): return list(map(list, input().split()))
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
    s = S()
    lens = len(s)
    if lens == 1:
        print(0)
        return
    d = [0] * ((lens - 1) // 2 + 1)
    for i in range((lens - 1) // 2 + 1):
        d[i] = s[-i - 1] == s[i]
    d = list(itertools.accumulate(d))
    if lens & 1:
        if d[-1] == (lens - 1) // 2 + 1:
            print(lens * 25 - 25)
            return
        if d[-1] == (lens - 1) // 2:
            print ((lens - 2) * 25 + 48)
            return
        print (lens * 25)
        return
    else:
        if d[-1] == (lens - 1) // 2 + 1:
            print(lens * 25)
            return
        if d[-1] == (lens - 1) // 2 :
            print(lens * 25 - 2)
            return
        print (lens * 25)
        return
    return


#main
if __name__ == '__main__':
    solve()
