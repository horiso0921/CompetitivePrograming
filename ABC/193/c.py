from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys
import random
import itertools
import math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
mod = 1000000007
inf = 1e10
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


def solve():
    n = II()
    t = [1] * (10 ** 5 + 1)
    ans = n
    for i in range(2, 10 ** 5 + 1):
        j = i * i
        f = 0
        while t[i]:
            f = 1
            if j > 10 ** 5:
                break
            t[j] = 0
            j *= i
        if f:
            f = 0
            x = i * i
            while x <= n:
                x *= i
                f += 1
            ans -= f
    print(ans)
    return


# main
if __name__ == '__main__':
    solve()
