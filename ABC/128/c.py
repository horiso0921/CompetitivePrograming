
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
def C():
    n, m = LI()
    ks = LIR_(m)
    p = LI()
    patern = itertools.product(range(2), repeat=n)
    ans = 0
    for on in patern:
        ki = [0 for i in range(m)]
        for num, oni in enumerate(on):
            if oni:
                for i,ksi in enumerate(ks):
                    ksi = ksi[1::]
                    if num in ksi:
                        ki[i] ^= 1
        for num, pi in enumerate(p):
            if pi != ki[num]:
                break
        else:
            ans += 1
    print(ans)

            
    return

