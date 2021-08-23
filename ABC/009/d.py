
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
K, m = map(int, input().split())
def productmatric(C,D):
    res = [[0 for i in range(K)] for k in range(K)]
    for i in range(K):
        for k in range(K):
            bf = 0
            for l in range(K):
                bf = bf ^ (C[i][l] & D[l][k])
            res[i][k] = bf
    return res
            

def powmatric(n, C, D):
    if n % 2:
        return powmatric(n // 2, productmatric(C, D), productmatric(D, D))
    else:
        if n == 0:
            return C
        return powmatric(n // 2, C, productmatric(D,D))
        
a = list(map(int, input().split()))
ak = []
for i in a:
    ak.append([i])
C = [list(map(int, input().split()))]
ak = ak[::-1]
for i in range(1, K):
    bfc = []
    for p in range(K):
        if i-1 == p:
            bfc.append(2 ** 32 - 1)
        else:
            bfc.append(0)
    C.append(bfc)
tani = [[0 for i in range(K)] for k in range(K)]
for i in range(K):
    tani[i][i] = 2 ** 32 - 1

if m <= K:
    print(a[m - 1])
    quit()
C = powmatric(m - K,tani, C)
ANS = 0
for i in range(K):
    ANS = ANS ^ (C[0][i] & ak[i][0])
print(ANS)
