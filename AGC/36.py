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
def A(s):

    # たぶん嘘解法です
    def fake():

        def pri(n, x):
            for i in range(2, int(math.sqrt(n))):
                if n % i == 0 and n // i <= x:
                    return [i, n // i]
            return [1, n]

        x = int(math.sqrt(s))
        if s < 10 ** 9:
            print(0, 0, 0, s, 1, 0)
            return
        while 1:
            X = x ** 2
            if X - s < 0:
                x += 1
                continue
            b = pri(X - s, x)
            if b:
                print(0, 0, x, int(b[0]), int(b[1]), x)
                return
            x += 1
        return

    # 本解答
    v = 10 ** 9
    y = -s % v
    x = (s + y) // v
    print(0, 0, v, 1, y, x)
    return

#B
def B():
    return

#C
def C():
    return

#D
def D():
    return

#E
def E():
    return

#F
def F():
    return



#Solve
if __name__ == '__main__':
    A(II())
