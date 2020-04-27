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
    a, b, c = LI()
    if a < b:
        if b < c:
            print(b)
        else:
            if a < c:
                print(c)
            else:
                print(a)
    else:
        if a < c:
            print(a)
        else:
            if b < c:
                print(c)
            else:
                print(b)
    return

#B
def B():
    s = S()
    ans = []
    x = 0
    bf = s[x]
    for i in s:
        if bf == i:
            x += 1
        else:
            ans.append(bf + str(x))
            bf = i
            x = 1
    ans.append(bf + str(x))
    print("".join(ans))

    return

#C
def C():
    II()
    an = LI()
    for num, a in enumerate(an):
        while a % 2 == 0:
            a = a // 2
        an[num] = a
    #print(an)
    print(len(set(an)))

    return

#D
def D():
    n = II()
    point = (0, -1)
    for i in range(2, n + 1):
        print("? {0} {1}".format(1, i), flush=True)
        x = II()
        if point[0] < x:
            point = (x, i)
    point = point[1]
    ans = 0
    for i in range(1, n + 1):
        if point == i:
            continue
        print("? {0} {1}".format(point, i), flush=True)
        ans = max(ans, II())
    print("! {}".format(ans))
    return

#Solve
if __name__ == '__main__':
    D()
