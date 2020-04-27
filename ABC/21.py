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
    n = II()
    n = bin(n)[2:]
    print(list(str(n)).count("1"))
    for num, i in enumerate(n):
        if i == "1":
            print(2**num)
    return

#B
def B():
    II()
    a, b = LI()
    II()
    p = LI()
    if a in p or b in p:
        print("NO")
        return
    if len(set(p)) != len(p):
        print("NO")
        return
    print("YES")
    return

#C
def C():
    n = II()
    a, b = LI_()
    m = II()
    xy = LIR_(m)
    ans = [inf for i in range(n)]
    edg = [[] for i in range(n)]
    for x, y in xy:
        edg[x].append(y)
        edg[y].append(x)
    q = deque()
    q.append(a)
    ans[a] = 0
    while q:
        now = q.pop()
        for go in edg[now]:
            if ans[go] > ans[now] + 1:
                ans[go] = ans[now] + 1
                q.append(go)
    r = deque()
    r.append(b)
    dag = [[] for i in range(n)]
    bdag = [[] for i in range(n)]
    check = [True for i in range(n)]
    while r:
        now = r.pop()
        for go in edg[now]:
            if ans[go] + 1 == ans[now]:
                dag[go].append(now)
                bdag[go].append(now)
                if check[go]:
                    r.append(go)
                    check[go] = False
    def topolosort():
        cut = deque()
        while True:
            flg = True
            for d in bdag:
                for dd in d:
                    if len(bdag[dd]) == 0:
                        cut.appendleft(dd)
                        for d_ in bdag:
                            if dd in d_:
                                d_.remove(dd)
                                flg = False
            if flg:
                break
        cut.appendleft(a)
        return cut
    topdag = topolosort()
    dp = [0 for _ in range(n)]
    dp[a] = 1
    for da in topdag:
        for dad in dag[da]:
            dp[dad] += dp[da]
            dp[dad] %= mod
    print(dp[b])
    return

#D
def D():
    def power_func(a, b):
        # a^b mod p を求める
        # bを2進数分解して高速累乗

        if b == 0: return 1
        if b % 2 == 0:
            d = power_func(a, b // 2)
            return d * d % mod
        if b % 2 == 1:
            return (a * power_func(a, b - 1)) % mod

    def combination_mod(n, k):
        # power_funcを用いて(nCk) mod p を求める 
        # nCk = n!/((n-k)!k!)を使用

        from math import factorial
        if n < 0 or k < 0 or n < k: return 0
        if n == 0 or k == 0: return 1
        a = factorial(n) % mod
        b = factorial(k) % mod
        c = factorial(n - k) % mod
        return (a * power_func(b, mod - 2) * power_func(c, mod - 2)) % mod
    
    n, k = IR(2)
    print(combination_mod(n + k - 1, n - 1))
    return

#Solve
if __name__ == '__main__':
    D()
