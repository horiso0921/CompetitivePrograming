#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**7)
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
    a, d = LI()
    print(max((a + 1) * d, a * (d + 1)))
    return

#B
def B():
    l, h = LI()
    for _ in range(II()):
        a = II()
        if a > h:
            print(-1)
        elif l <= a <= h:
            print(0)
        else:
            print(l-a)
    return

#C
def C():
    n = II()
    a = LI()
    ans = -inf
    for i in range(n):
        aoki = -inf
        takahashi = -inf
        for k in range(n):
            if i == k:
                continue
            if aoki < sum(a[min(i, k) + 1:max(i, k) + 1:2]):
                aoki = sum(a[min(i, k) + 1:max(i, k) + 1:2])
                takahashi = sum(a[min(i, k):max(i, k) + 1:2])
        ans = max(ans, takahashi)
    print(ans)
    return

# D
# 数を決め打ちすればいい
# 結局DFSとやってること変わんなくねｗ

def D():
    def dfs(j):
        for num, vwi in enumerate(vw[j:]):
            v, w = vwi
            x = 0
            lw = len(w)
            for vi in v:
                vi = int(vi)
                if l[vi]:
                    lv = l[vi]
                    if ans[vi] == w[x:lv+x]:
                        x += lv
                    else:
                        return False
                    continue
                for i in range(1, 4):
                    ans[vi] = w[x:x + i]
                    l[vi] = i
                    if dfs(num + j):
                        return True
                ans[vi] = None
                l[vi] = 0
                return False
            if x != lw:
                return False
        return True

    k, n = LI()
    vw = LSR(n)
    ans = [None] * (k + 1)
    l = [0] * (k + 1)
    dfs(0)
    for i in ans[1:]:
        print("".join(i))
    return

def D_():
    k, n = LI()
    vw = LSR(n)
    lengths = itertools.product(range(1, 4), repeat=k)
    for length in lengths:
        ans = defaultdict(str)
        f = False
        for v, w in vw:
            for vi in v:
                l = length[int(vi) - 1]
                if ans[vi]:
                    if ans[vi] == w[:l]:
                        w = w[l:]
                        continue
                    else:
                        f = True
                        break
                ans[vi] = w[:l]
                w = w[l:]
            if f or w:
                break
        else:
            ans = list(ans.items())
            ans.sort()
            for _, i in ans:
                print("".join(i))
            return


    
    

#Solve
if __name__ == '__main__':
    D()
