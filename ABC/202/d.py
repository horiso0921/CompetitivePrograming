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

fact = [i for i in range(70)]
fact[0] = 1
for i in range(69):
    fact[i+1] *= fact[i]

def nCk(n, k) -> int:
    return fact[n] // fact[k] // fact[n - k]
#solve
def solve():
    a,b,k = LI()
    ans = []
    A = a
    B = b
    for i in range(a+b):
        if nCk(a+b-1-i, B) < k:
            ans.append("b")
            k -= nCk(a+b-1-i, B)
            B -= 1
        else:
            ans.append("a")
            A -= 1
    print("".join(ans))

    return


#main
if __name__ == '__main__':
    solve()