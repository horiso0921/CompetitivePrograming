#!usr/bin/env python3
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
    a = input().split()
    a = list(map(lambda x: x.capitalize(), a))
    a,b,c = a
    print(a[0]+b[0]+c[0])
    return

#B
def B():
    a = II()
    b = II()
    if a > b:
        print("GREATER")
    if a < b:
        print("LESS")
    if a == b:
        print("EQUAL")
    return

#C
def C():
    II()
    a = LI()
    def f(suma, b):
        for i in a[1:]:
            if suma * (suma + i) < 0:
                suma += i
                continue
            b += (abs(suma + i) + 1)
            suma = (-1 * (suma > 0)) or 1
        return b

    if a[0] == 0:
        ans = min(f(1, 1), f(-1, 1))
    else:
        ans = min(f(a[0], 0), f(1 * (a[0] < 0) or - 1, abs(a[0]) + 1))
    print(ans)
    return

#D
def D_():
    s = S()
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            print(i + 1, i + 2)
            return
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            print(i + 1, i + 3)
            return
    print(-1, -1)

def D():
    x, y = LI()
    a = abs(x - y)
    if a <= 1:
        print("Brown")
    else:
        print("Alice")
    return


#Solve
if __name__ == '__main__':
    C()
