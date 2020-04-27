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
    n, k = LI()
    a = n - k
    if k == 1:
        print(0)
        return
    print(a)
    return

#B
def B():
    n = II()
    xy = LIR(n)
    if n == 1:
        print(1)
        return
    ans = inf
    for i in range(n):
        for k in range(n):
            if i != k:
                b = 1
                check = []
                check.append((i,k))
                p = xy[i][0] - xy[k][0]
                q = xy[i][1] - xy[k][1] 
                for l in range(n):
                    for m in range(n):
                        if not((l,m) in check) and p == xy[l][0] - xy[m][0] and q == xy[l][1] - xy[m][1]:
                            b += 1
                            check.append((l, m))
                ans = min(ans, n-b)
    print(ans)

    return

#C
def C():
    n = II()
    a = LI()
    a.sort(key=abs)
    ans = deque()
    positive = deque()
    negative = deque()
    for i in range(n):
        if a[i] >= 0:
            positive.append(a[i])
        else:
            negative.append(a[i])
    a = deque(a)
    lenp = len(positive)
    lenn = len(negative)
    if lenp == 0:
        for i in range(n - 1):
            b, c = a.popleft(), a.popleft()
            ans.append((b, c))
            b -= c
            a.appendleft(b)
        print(b)
    elif lenn == 0:
        for i in range(n - 2):
            b, c = a.popleft(), a.popleft()
            ans.append((b, c))
            b -= c
            a.appendleft(b)
        b, c = a.popleft(), a.popleft()
        ans.append((c, b))
        c -= b
        print(c)
    else:
        p = positive.popleft()
        negative.appendleft(p)
        for i in range(lenn - 1):
            b, c = negative.popleft(), negative.popleft()
            ans.append((b, c))
            b -= c
            negative.appendleft(b)
        p, c = negative.popleft(), negative.popleft()
        positive.appendleft(c)
        for i in range(lenp - 1):
            b, c = positive.popleft(), positive.popleft()
            ans.append((b, c))
            b -= c
            positive.appendleft(b)
        b = positive.popleft()
        ans.append((p, b))
        p -= b
        print(p)
    for an in ans:
        print(" ".join(map(str, an)))
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

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    C()
