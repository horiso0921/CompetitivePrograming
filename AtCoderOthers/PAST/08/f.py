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
    n = II()
    s = S()
    ans = [None] * n
    q = deque()
    for i in range(n):
        si = s[i]
        if si == "0":
            q.append(i)
        else:
            ans[i] = i+1
    for i in range(n):
        si = s[i]
        if si == "0":
            if q:
                if q[0] != i:
                    ans[i] = q.popleft() + 1
                elif q[-1] != i:
                    ans[i] = q.pop() + 1
                else:
                    print(-1)
                    return
    if None in ans:
        print(-1)
        return
    print(*ans)
                     
    return


#main
if __name__ == '__main__':
    solve()