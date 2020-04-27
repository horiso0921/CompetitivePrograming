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
    a = S()
    b = S()
    if len(a) > len(b):
        print("".join(a))
    else:
        print("".join(b))
    return
 
#B
def B():
    a = II()
    b = LI()
    while 0 in b:
        b.remove(0)
    print(math.ceil(sum(b)/len(b)))
    return
 
#C
def C():
    n, k = LI()
    t = LIR(n)
    five_ = list(itertools.product(range(k), repeat=n))
    for five in five_:
        ans = 0
        for num,f in enumerate(five):
            ans = ans ^ t[num][f]
        if not ans:
            print("Found")
            return
    print("Nothing")        
    return
 
#D
def D():
    W = II()
    N, K = LI()
    ab = LIR(N)
    dp = [[0 for i in range(W + 1)] for l in range(K + 1)]
    for num, ab_ in enumerate(ab):
        a = ab_[0]
        b = ab_[1]
        for w in range(W, -1, -1):
            for k in range(K, 0, -1):
                if a <= w:
                    dp[k][w] = max(dp[k][w], dp[k - 1][w - a] + b)
                else:
                    dp[k][w] = dp[k][w] 

    print(dp[K][W])
              
 
    return
 
#E
def E():
    return
 
#F
def F():
    return
 
#G
def G():
    return
 
#H
def H():
    return
 
#Solve
if __name__ == '__main__':
    D()