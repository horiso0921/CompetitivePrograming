#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    n = II()
    if n < 60:
        print("Bad")
    elif n < 90:
        print("Good")
    elif n < 100:
        print("Great")
    else:
        print("Perfect")
    return

#B
def B():
    s = S()
    d = defaultdict(int)
    alp = ["A", "B", "C", "D", "E", "F"]
    for a in alp:
        d[a] = 0
    for si in s:
        d[si] += 1
    print(" ".join(map(str, d.values())))
    return

#C
def C():
    abcde = LI()
    ans = []
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j + 1, 5):
                ans.append(abcde[i] + abcde[j] + abcde[k])
    ans.sort()
    print(ans[-3])
    return

#D
def D():
    n, k = LI()
    print(((n - k) * 3 + (k - 1) * 3 + (k - 1) * (n - k) * 6 + 1) / n ** 3)

    return

#Solve
if __name__ == '__main__':
    D()
