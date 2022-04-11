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
    n,m = LI()
    a = LI()
    b = LI()
    qa = deque()
    qb = deque()
    for i in range(n):
        if a[i] != 0:
            qa.append((a[i], i))
    qa.append((n+m+1, n))
    for i in range(m):
        if b[i] != 0:
            qb.append((b[i], i))
    qb.append((n+m+1, m))
    
    ans = [[0] * n, [0] * m]
    
    i = 0
    j = 0
    an = 1
    while i < n or j < m:

        if qa[0][0] == an:
            ans[0][i] = an
            qa.popleft()
            i += 1
            an += 1
            continue
        
        if qb[0][0] == an:
            ans[1][j] = an
            qb.popleft()
            j += 1
            an += 1
            continue
        
        
        if qa[0][1] == i:
            ans[1][j] = an
            j += 1
            an += 1
            continue
            
        if qb[0][1] == j:
            ans[0][i] = an
            i += 1
            an += 1
            continue
        
        if qa[0][0] < qb[0][0]:
            ans[0][i] = an
            i += 1
            an += 1
        else:
            ans[1][j] = an
            j += 1
            an += 1
    print(*ans[0])
    print(*ans[1])
    return


#main
if __name__ == '__main__':
    solve()