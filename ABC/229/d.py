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
    s = S()
    k = II()
    ans = 0
    tmp = deque()
    aa = 0
    for i in range(len(s)):
        if s[i] == ".": aa += 1
        tmp.append(i)
        if aa == k + 1:
            while tmp and aa == k + 1:
                x = tmp.popleft()
                if s[x] == ".":
                    aa -= 1
    
        ans = max(ans, len(tmp))
    print(max(ans, len(tmp)))
    return


#main
if __name__ == '__main__':
    solve()