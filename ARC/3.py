#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys, math, bisect, random, itertools
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
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

#A
def A():
    n = II()
    r = input().rstrip()
    d = {"A": "4", "B": "3", "C": "2", "D": "1", "F": "0"}
    for key, value in d.items():
        r = r.replace(key, value)
    print(sum(list(map(int, list(r)))) / n)
    return

#B
def B():
    n = II()
    ss = []
    for _ in range(n):
        s = input().rstrip()[::-1]
        ss.append(s)
    ss.sort()
    for si in ss:
        print(si[::-1])
    return

#C
def C():
    return

#D
def D():
    return


#Solve
if __name__ == '__main__':
    B()
