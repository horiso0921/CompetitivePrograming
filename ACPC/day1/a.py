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

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    n = I()
    s = [input().split() for _ in range(n)]
    a = []
    t = input()
    for i in s:
        a += i
    for p in permutations(a,3):
        if "".join(p) == t:
            print("Yes")
            return
    print("No")
    return

#Solve
if __name__ == "__main__":
    solve()
