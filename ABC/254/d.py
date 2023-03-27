#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
#solve
def solve():
    n = II()
    ans = []
    d = defaultdict(int)
    for i in range(1, n+1):
        ans.append(i * i)
        d[i * i] = 1
    ans_n = 0
    for i in range(1,n+1):
        if d[i]:
            j = bisect_right(ans, n)
            ans_n += j
            # print(ans, j)
        else:
            x = factorization(i)
            tmp = 1
            for xi in x:
                if xi[1] & 1:
                    tmp *= xi[0]
            j = bisect_right(ans, n // tmp)
            ans_n += j
    print(ans_n)
        
    return


#main
if __name__ == '__main__':
    solve()