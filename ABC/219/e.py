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
    a = LIR(4)
    ans = 0
    for mask in range(1 << 16):
        tmp = []
        for i in range(16):
            x,y = i % 4, i // 4
            if mask & 1 << i: 
                tmp.append((y,x))
            else:
                if a[y][x] == 1:
                    break
        else:
            d = defaultdict(int)
            for t in tmp:
                d[t] = 1
            q = [tmp[0]]
            d[tmp[0]] = 0
            for y,x in q:
                for mx,my in [(0,1),(1,0),(-1,0),(0,-1)]:
                    mx += x
                    my += y
                    if 0 <= mx < 4 and 0 <= my < 4:
                        if d[(my, mx)]:
                            d[(my, mx)] = 0
                            q.append((my,mx))
            if sum(d.values()):
                continue
            x,y = -1,-1
            q = [(y,x)]
            d = defaultdict(int)
            d[(y,x)] = 1
            for y,x in q:
                for mx,my in [(0,1),(1,0),(-1,0),(0,-1)]:
                    mx += x
                    my += y
                    if -1 <= mx < 5 and -1 <= my < 5:
                        if d[(my, mx)]: continue
                        if 0 <= mx < 4 and 0 <= my < 4:
                            if mask & 1 << (my * 4 + mx): continue
                        d[(my, mx)] = 1
                        q.append((my,mx))
            for i in range(16):
                if not(mask & 1 << i):
                    x,y = i % 4, i // 4
                    if d[(y,x)] == 0: 
                        break 
            else:
                ans += 1
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()