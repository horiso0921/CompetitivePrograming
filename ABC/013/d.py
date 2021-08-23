
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

N, m, d = LI()
a = LI()
numlis = [i for i in range(N + 1)]
def amida(num, a):
    for i in a:
        bf = num[i]
        bff = num[i + 1]
        num[i] = bff
        num[i + 1] = bf
        #print(num)
    returnlis = [i for i in range(N + 1)]
    for i in num:
        returnlis[i] = num.index(i)
    return returnlis
def binami(x):
    returnlis = [i for i in range(N + 1)]
    for num,i in enumerate(x):
        returnlis[num] = x[i]
    return returnlis
binamida = [amida(numlis, a)]
for i in range(30):
    binamida.append(binami(binamida[-1]))
#print(binamida)      
d = bin(d)
d = list(map(int, d[2::]))
d = d[::-1]

#print(d)
for k in range(1, N + 1):
    x = k
    for num, i in enumerate(d):
        if i == 1:
            x = binamida[num][x]
    print(x)
