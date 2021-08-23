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
    # n = II()
    # a = LI()
    # dp = [[[0] * n for i in range(n)] for i in range(n)]
    # tmp = [[0] * 4]
    # for ai in a:
    #     tmp[0][ai+1] += 1
    # q = deque(tmp)
    # dp[tmp[1]][tmp[2]][tmp[3]] = 0
    # while q:
    #     s,a1,a2,a3 = q.pop()
    #     dp[a1-1][a2][a3] = (a2-a3) / a1 * s
    #     dp[a1][a2][a3] = (a2-a3) / a2 * s
    #     dp[a1][a2-][a3] = (a2-a3) / a3 * s
    ans = []
    with open("t.txt", "r", encoding="utf-8") as t:
        for ti in t:
            ti = ti.split("\t")
            ans.append((int(ti[3]), ti[2]))
    ans.sort(reverse=True)
    with open("t", "w", encoding="utf-8") as t:
        for i in range(len(ans)):
            t.write(str(i) + "   ")
            t.write(str(ans[i][0]) + "  ")
            t.write(str(ans[i][1]))
            t.write("\n")

    return


#main
if __name__ == '__main__':
    solve()