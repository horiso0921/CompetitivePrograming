#!usr/bin/env python3
from collections import defaultdict
from heapq import heappush, heappop
import sys
import math
import bisect
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return list(sys.stdin.readline())
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
mod = 1000000007

#A
"""
alp = [0, "A", "B", "C", "D", "E"]
x = input()
print(alp.index(x))
"""

#B
"""
a = int(input())
b = int(input())
c = b
ans = 0
while a != b and a != c:
    ans += 1
    b += 1
    c -= 1
    if b == 10:
        b = 0
    if c == -1:
        c = 9
print(ans)
"""

#C
"""
n, h = map(int, input().split())
a, b, c, d, e = map(int, input().split())
A = h - n * e
if A >= 1:
    print(0)
else:
    A = abs(A) + 1
    b += e
    d += e
    ans = (float("INF"), float("INF"))
    ansnum = float("INF")
    for i in range(0, n + 1):
        x = i
        y = (A - d * x - 1) // b + 1
        if x + y <= n and y >= 0:
            ansnum = min(ansnum, x * c + y * a)
    print(ansnum)
"""

#D

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
