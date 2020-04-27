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
    n, a, b = LI()
    print(min(n*a,b))
    return

#B
def B():
    a = S()
    print(a.count("1"))
    return

#C
def C():
    n = II()
    a = list(str(n))
    a = list(map(int,a))
    if not n % sum(a):
        print("Yes")
    else:
        print("No")
    return

#D
def D():
    n = II()
    a = LI()
    ans = 0
    while True:
        for i in range(n):
            if a[i] % 2:
                print(ans)
                return    
            a[i] /= 2
        ans += 1
    print(ans)
    return

#E
def E():
    n = II()
    f = LIR(n)
    p = LIR(n)
    bi = itertools.product([0, 1], repeat=10)
    
    return

#F
def F():
    n, k = LI()
    a = LI()
    dic = defaultdict(int)
    for a_ in a:
        dic[a_] += 1
    dic = sorted(dic.values(),reverse = True)
    l = 0
    ans = 0
    for j in dic:
        l += 1
        ans += j
        if l == k:
            break
    print(n-ans)
    

    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    F()
