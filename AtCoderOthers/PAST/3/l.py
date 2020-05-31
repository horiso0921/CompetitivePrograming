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
    l1 = [[None, None] for i in range(n)] 
    l2 = [[None, None] for i in range(n)] 
    container = [[] for i in range(n)]
    d = defaultdict(int)
    for i in range(n):
        t, *k = LI()
        k = [(k[j], j) for j in range(t)]
        container[i] = deque(k)
    m = II()
    a = LI()
    for i in range(n):
        q, j = container[i].popleft()
        heappush(q1, (-q, i, j))
        heappush(q2, (-q, i, j))
        if container[i]:
            q, j = container[i].popleft()
            l2[i] = (-q, j)
            heappush(q2, (-q, i, j))
    for i in a:
        if i == 1:
            x, i, j = heappop(q1)
            x = -x
            while d[(i, j)]:
                x, i, j = heappop(q1)
                x = -x
            d[(i, j)] = 1
            if l2[i][0] != None:
                heappush(q1, (-l2[i][0], i, l2[i][1]))
                l2[i] = (None, None)
                if container[i]:
                    q, j = container[i].popleft()
                    l2[i] = (-q, j)
                    heappush(q2, (-q, i, j))
            print(x)
        else:
            x, i, j = heappop(q2)
            x = -x
            while d[(i, j)]:
                x, i, j = heappop(q2)
                x = -x
            if l2[i][1] == j:
                heappush(q1, (l2[i][0], i, l2[i][1]))
                d[(i, j)] = 1
                l2[i] = (None, None)
                if container[i]:
                    q, j = container[i].popleft()
                    l2[i] = (-q, j)
                    heappush(q2, (-q, i, j))
            else:
                while d[(i, j)]:
                    x, i, j = heappop(q1)
                    x = -x
                d[(i, j)] = 1
                if l2[i][0] != None:
                    heappush(q1, (-l2[i][0], i, l2[i][1]))
                    l2[i] = (None, None)
                    if container[i]:
                        q, j = container[i].popleft()
                        l2[i] = (-q, j)
                        heappush(q2, (-q, i, j))
            print(x)

        

    return


#main
if __name__ == '__main__':
    solve()
