
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

def comb(n,k):
    """power_funcを用いて(nCk) mod p を求める"""
    from math import factorial
    if n<0 or k<0 or n<k: return 0
    if n==0 or k==0: return 1
    a=factorial(n) 
    b = factorial(k)
    c=factorial(n-k)
    return (a / (b * c))
import math

n, d = map(int, input().split())
x, y = map(int, input().split())
x = abs(x)
y = abs(y)
ansn = n
if x % d == 0 and y % d == 0:
    ax = x // d
    ay = y // d
    ansb= 0
    nb = n - ax - ay
    if nb % 2 == 0:
        nb = nb // 2
        for i in range(nb + 1):
            ans = math.exp(math.log(comb(n, i + ax))+math.log(comb(n - i - ax, i))+math.log(comb(n - 2 * i - ax, ay + nb - i))-n*math.log(4))
            ansb += ans
        print(ansb)
    else:
        print(0)
else:
    print(0)
