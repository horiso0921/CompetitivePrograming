#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
from math import atan2, degrees
import sys 
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
    n = S()
    if len(list(set(n))) == 1:
        print("SAME")
    else:
        print("DIFFERENT")
    return

#B
def B():
    n = II()
    a = LSR(n)
    a = list(map(lambda x:[x[0],int("".join(x[1]))], a))
    a.sort(key=lambda x: x[1], reverse=True)
    ma = a[0][1]
    su = 0
    for _,x in a:
        su += x
    if su/2 >= ma:
        print("atcoder")
    else:
        print("".join(a[0][0]))
    return

#C
def C():
    s = input().split("+")
    ans = 0
    for si in s:
        if "0" in si:
            continue
        ans += 1
    print(ans)
    return

# D
# 解説AC
# 鈍角三角形には鈍角が一つだけ
# 直角三角形には直角が一つだけ
# あることがミソ
# 鈍角になる3点と直角になる3点の数を出せばよい
# 1点を決めてn点間の水平からの角度を出す((-1,0)が-180°)
# そのn点から時計回りに90°,90°~180°になる点の数は
# 尺取り法なり二分探索なりで求められるためそれで終わり
def D():
    n = II()
    xy = LIR(n)
    right = 0
    obtuse = 0
    for x, y in xy:
        lis = []
        for xi, yi in xy:
            if x == xi and y == yi:
                continue
            the = degrees(atan2(yi - y, xi - x))
            lis.append(the)
            lis.append(the + 360)
        lis.sort()
        llis = len(lis)
        for l in lis[:llis // 2]:
            right += bisect_right(lis, l + 90 + 1e-9) - bisect_left(lis, l + 90 - 1e-9)
            obtuse += bisect_right(lis, l + 180 + 1e-9) - bisect_right(lis, l + 90 + 1e-9)
    print(n * (n - 1) * (n - 2) // 6 - right - obtuse, right, obtuse)
    return

#Solve
if __name__ == '__main__':
    D()
