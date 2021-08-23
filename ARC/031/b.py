#!/usr/bin/env python3
from collections import defaultdict, deque
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
    a = SR(10)
    ans = 0
    for y in range(10):
        for x in range(10):
            ans += a[y][x] == "o"
    for y_ in range(10):
        for x in range(10):
            y = y_
            if a[y][x] == "x":
                q = deque()
                q.append((y, x))
                d = defaultdict(int)
                d[(y,x)] = 1
                tmp = 0
                while q:
                    y, x = q.pop()
                    for mx, my in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        mx += x
                        my += y
                        if 0 <= mx < 10 and 0 <= my < 10:
                            if (not d[(my,mx)]) and a[my][mx] == "o":
                                q.appendleft((my, mx))
                                tmp += 1
                            d[(my, mx)] = 1
                if tmp == ans:
                    print("YES")
                    return
    print("NO")
    return


#main
if __name__ == '__main__':
    solve()