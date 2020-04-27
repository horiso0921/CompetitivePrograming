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
    a, b, c = LI()
    if a == b:
        print(c)
    elif a == c:
        print(b)
    else:
        print(a)
    return

#B
def B():
    n = II()
    a = LI()
    if sum(a) % n:
        print(-1)
        return
    av = sum(a)//n
    ans = 0
    i = 0
    while i < n:
        b = 0
        for k in range(n-i):
            b += a[k + i]
            if  b / (k + 1) == av:
                i += k + 1
                break
            ans += 1
    print(ans)
    return

# C
# 解説AC
# ゲーム木を作成してシミュレーションしてみよう 
def C(n):
    now = 1
    i = 1
    ans = ["Aoki", "Takahashi"]
    stratege = int(math.log(n, 2)) & 1
    while now <= n:
        if i:
            now = now * 2 + stratege ^ 1
        else:
            now = now * 2 + stratege
        i ^= 1
    print(ans[i])
    return

# D
# 解説AC
# DPではダメで考察が重要
# Mでの移動が後ろの+-のすべてに寄与する
# あるMの後ろすべての+-の数がわかれば
# そのMが合計の値にどれほど影響するかがわかるかがミソ 
def D():
    s = S()
    a = []
    x = 0
    for si in s[::-1]:
        if si == "+" or si == "-" :
            x += 1 if si == "+" else - 1
        if si == "M":
            a.append(x)
    a = a[::-1]
    a.sort()
    l = len(a)//2
    print(-sum(a[:l]) + sum(a[l:]))
    return

#Solve
if __name__ == '__main__':
    D()
