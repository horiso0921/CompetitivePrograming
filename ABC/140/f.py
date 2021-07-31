
#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
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

#solve
def F():
    def root(x):
        if x == par[x]:
            return x
        par[x] = root(par[x])
        return par[x]
    def unite(x, y):
        x = root(x)
        y = root(y)
        if x == y: return
        if x > y: y, x = x, y
        par[x] = y
        return
    n = II()
    s = LI()
    s.sort(reverse=True)
    x = list(sorted(set(s)))[::-1]
    d = defaultdict(int)
    di = defaultdict(int)
    for i, xi in enumerate(x):
        d[xi] = i
    ma = i + 1
    num = [0] * (ma)
    par = [i for i in range(ma)]
    for si in s:
        num[d[si]] += 1
    l = [0]
    num[0] -= 1
    for _ in range(n):
        tmp = l[::1]
        for li in l:
            if root(li) + 1 < ma and num[root(li) + 1]:
                num[root(li)+1] -= 1
                tmp.append(root(li)+1)
            else:
                i = 0
                x = root(li)
                while root(x + i) + 1 < ma and (not num[root(x + i) + 1]):
                    i += 1
                unite(li, x + i)
                if root(li)+1 >= ma:
                    print("No")
                    return
                tmp.append(root(li)+1)
                num[root(li)+1] -= 1
        l = tmp[::1]
    print("Yes")
    return

