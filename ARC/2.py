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
    y = II()
    if y % 400 == 0:
        print("YES")
        return
    if y % 100 == 0:
        print("NO")
        return
    if y % 4 == 0:
        print("YES")
        return
    print("NO")
    return

#B
def B():
    y, m, d = map(int, input().rstrip().split("/"))
    t = [4, 6, 9, 11]
    def f(y, m, d):
        y /= m
        y /= d
        return not y.is_integer()

    while f(y, m, d):
        d += 1
        if m in t:
            if d == 31:
                d = 1
                m += 1
        else:
            if m == 2:
                if y % 400 == 0 or y % 100 != 0 and y % 4 == 0:
                    if d == 30:
                        d = 1
                        m += 1
                else:
                    if d == 29:
                        d = 1
                        m += 1
            else:
                if d == 32:
                    d = 1
                    m += 1
                    if m >= 13:
                        m = 1
                        y += 1
    print("{:04d}/{:02d}/{:02d}".format(y, m, d))
    return

#C
def C():
    n = II()
    c = S()
    short = itertools.product(["A", "B", "X", "Y"], repeat=2)
    short_comb = itertools.combinations(short, 2)
    ans = inf
    for sc in short_comb:
        i = 0
        tmp = 0
        while i < n - 1:
            if (c[i], c[i + 1]) in sc:
                i += 1
            i += 1
            tmp += 1
        tmp += i == n - 1
        ans = min(ans, tmp)
    print(ans)
    return

#D
def D():
    return


#Solve
if __name__ == '__main__':
    C()
