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

#A
def A():
    n = II()
    a = n // 2
    b = n - a
    print(a*b)
    return

#B
def B():
    x1, y1, x2, y2 = LI()
    a = x2 - x1
    b = y2 - y1
    print(x2 - b, y2 + a, x1 - b, y1 + a)
    return

#C
def C():
    n, k = LI()
    if k % 2:
        print((n // k)** 3)
    else:
        print(int((n//k)**3 + ((n-k/2)//k+1)**3))
        
    return

# D
# 解説AC
# a→bの辺に関していえばこの辺を2辺張ってしまえば2*n本で
# 2^n個のパスの組み合わせができることに気づけなかった
# i→i+1へ辺を出して長さは0 or 1<<i-1の辺を張ることで
# 和のi番目のbitを立たせるかを選ばせることができる
# さらに、Lのi番目のbitが立っているときにi番目のbitを立たせる
# もしくは最上位のbitを立たせてかつ、そのbitを除くi番目より上位の
# 立っているbitすべてを立たせたものの和を辺の長さとして辺を張ることで
# 解が得られる（はず）
def D():
    l = II()
    lBit = bin(l)[:1:-1]
    #print(lBit)
    n = len(lBit)
    ans = []
    for i in range(1, n):
        ans += [(i, i + 1, 0)] + [(i, i + 1, 1 << i - 1)]
    b = 1 << n - 1
    for i in range(n - 1):
        if lBit[-2 - i] == "1":
            ans += [(n - i - 1, n, b)]
            b += 1 << (n - i - 2)
    print(n,len(ans))
    for a in ans:
        print(*a)
    return


#Solve
if __name__ == '__main__':
    D()
