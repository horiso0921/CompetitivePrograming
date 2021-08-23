
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
def D():
    def divisor(n):
        res = []
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                res.append(i)
                res.append(n // i)
        return list(set(res))
    def Factoring(n):
        res = []
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                res.append(i)
            while n % i == 0:
                n //= i
        if n == 1:
            return res
        res.append(n)
        return res
    n, k = LI()
    divlis = divisor(k)
    ans = 0
    for divi in divlis:
        Prime_factors = Factoring(k // divi)
        lenPf = len(Prime_factors)
        res = (n // divi) * (n // divi + 1) // 2
        for i in range(1, lenPf + 1):
            select = itertools.combinations(range(lenPf), i)
            for sl in select:
                tmp = 1
                for s in sl:
                    tmp *= Prime_factors[s]
                res += (-1 * (i % 2) or 1) * tmp * (n // divi // tmp + 1) * (n // divi // tmp) // 2
        ans += res * k % mod
        ans %= mod
    print(ans)
    return


