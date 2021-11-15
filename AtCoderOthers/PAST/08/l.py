#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def IR(n):
    return [I() for _ in range(n)]
def LIR(n):
    return [LI() for _ in range(n)]

sys.setrecursionlimit(10000)
mod = 1000000007

def main():
    n,k = LI()
    a = LI()
    s = a[:]
    for i in range(n-1):
        s[i+1] += s[i]
    s.sort()
    l = 0
    r = 10**15
    while l+1 < r:
        x = (l+r) >> 1
        res = 0

        for i in range(n):
            res += bisect.bisect_right(s, s[i]+x) - bisect.bisect_left(s, s[i]-x)
        if res >= 2*k:
            r = x
        else:
            l = x
    print(r)
    return


if __name__ == "__main__":
    main()
