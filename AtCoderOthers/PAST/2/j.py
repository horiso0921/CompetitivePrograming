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
    s = S()
    n = len(s)
    def dfs(i):
        res = []
        f = 0
        for j in range(i, n):
            if s[j] == ")":
                if f == 0: return "".join(res)
                f -= 1
            elif s[j] == "(":
                if f:
                    f += 1
                else:
                    f += 1
                    tmp = dfs(j + 1)
                    res.append(tmp)
                    res.append(tmp[::-1])
            else:
                if f:
                    pass
                else:
                    res.append(s[j])
        return "".join(res)
    print(dfs(0))
    return


#main
if __name__ == '__main__':
    solve()
