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
    h,w = LI()
    s = [list(S()) for _ in range(h)]
    pre = deque()
    for hi in range(h-1, -1, -1):
        now = deque()
        for wi in range(w):
            if "0" <= s[hi][wi] < ":":
                now.append(s[hi][wi])
            elif s[hi][wi] in ["+", "-", "*"]:
                l = int(pre.popleft())
                r = int(pre.popleft())
                if s[hi][wi] == "*":
                    tmp = l * r
                elif s[hi][wi] == "-":
                    tmp = l - r
                elif s[hi][wi] == "+":
                    tmp = l + r
                now.append(tmp)
        pre = now
    print(now.pop())
    return


#main
if __name__ == '__main__':
    solve()