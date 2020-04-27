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
    _, b, c = LS()
    x = int(b[0] + c[0]) % 4
    if not x:
        print("YES")
    else:
        print("NO")
    return

#B
def B():
    II()
    a = LI()
    a.sort()
    print(a[-1]-a[0])
    return

#C
def C():
    II()
    a = LI()
    a = list(map(lambda x: x // 400, a))
    d = defaultdict(int)
    for ai in a:
        d[ai] += 1
    ans1 = 0
    ans2 = 0
    for key, value in d.items():
        if key <= 7:
            ans1 += 1
            ans2 += 1
        else:
            ans2 += value
    if ans1 == 0:
        ans1 = 1
    print(ans1, ans2)
    return

#D
def D():
    II()
    s = S()
    ans = deque(s[::1])
    f = 0
    for i in s:
        if i == "(":
            f += 1
        else:
            f -= 1
        if f < 0:
            ans.appendleft("(")
            f += 1
    ans.append(")" * f)
    print("".join(ans))

    return

#Solve
if __name__ == '__main__':
    D()
