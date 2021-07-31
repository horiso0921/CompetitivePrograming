
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
def B():
    s = S()
    i = len(s) - 1
    state = 0
    ans = 0
    bc = 1
    while i >= 0:
        if state == 0:
            if s[i] == "C":
                state += 1
        elif state == 1:
            if s[i] == "B":
                state += 1
            else:
                state = 0
        elif state == 2:
            if s[i] == "A":
                ans += 1
            elif s[i] == "B":
                state = 0
            else:
                state += 1
        elif state == 3:
            if s[i] == "B":
                state += 1
            elif s[i] == "C":
                bc = 1
                state = 1
            else:
                bc = 1
                state = 0
        else:
            if s[i] == "A":
                ans += bc
            elif s[i] == "B":
                state = 0
                bc = 1
            else:
                bc += 1
                state = 3
        #print(state,s[i])
        i -= 1
    print(ans)

    return

