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
    n = II()
    q1 = []
    q2 = []
    l2 = [None for i in range(n)] 
    container = [[] for i in range(n)]
    d = defaultdict(int)
    for i in range(n):
        t, *k = LI()
        container[i] = deque(k)
    m = II()
    a = LI()
    for i in range(n):
        q = container[i].popleft()
        heappush(q1, (-q, i))
        heappush(q2, (-q, i))
        if container[i]:
            q = container[i].popleft()
            l2[i] = q
            heappush(q2, (-q, i))
    for i in a:
        if i == 1:
            x, i = heappop(q1)
            x = -x
            while d[x]:
                x, i = heappop(q1)
                x = -x
            d[x] = 1
            if l2[i] != None:
                heappush(q1, (-l2[i], i))
                l2[i] = None
                if container[i]:
                    q = container[i].popleft()
                    l2[i] = q
                    heappush(q2, (-q, i))
            print(x)
        else:
            x, i = heappop(q2)
            x = -x
            while d[x]:
                x, i = heappop(q2)
                x = -x
            d[x] = 1
            if l2[i] == x:
                l2[i] = None
                if container[i]:
                    q = container[i].popleft()
                    heappush(q2, (-q, i))
                    l2[i] = q
            else:
                if l2[i] != None:
                    heappush(q1, (-l2[i], i))
                    l2[i] = None
                    if container[i]:
                        q = container[i].popleft()
                        heappush(q2, (-q, i))
                        l2[i] = q
            print(x)

        

    return


#main
if __name__ == '__main__':
    solve()
