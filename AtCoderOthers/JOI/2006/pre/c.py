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
    n = II()
    state = [1, 2, 3, 4, 5, 6]
    def tern(diarect):
        tmp = state[::1]
        if diarect == "East":
            state[0] = tmp[3]
            state[2] = tmp[0]
            state[3] = tmp[5]
            state[5] = tmp[2]
        elif diarect == "Left":
            state[1] = tmp[3]
            state[2] = tmp[1]
            state[3] = tmp[4]
            state[4] = tmp[2]
        elif diarect == "North":
            state[0] = tmp[1]
            state[1] = tmp[5]
            state[4] = tmp[0]
            state[5] = tmp[4]
        elif diarect == "Right":
            state[1] = tmp[2]
            state[2] = tmp[4]
            state[3] = tmp[1]
            state[4] = tmp[3]
        elif diarect == "South":
            state[0] = tmp[4]
            state[1] = tmp[0]
            state[4] = tmp[5]
            state[5] = tmp[1]
        elif diarect == "West":
            state[0] = tmp[2]
            state[2] = tmp[5]
            state[3] = tmp[0]
            state[5] = tmp[3]
        return state[0]
    ans = 1
    for _ in range(n):
        ans += tern(S())
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
